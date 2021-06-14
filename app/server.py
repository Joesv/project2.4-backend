from flask import Flask, request, jsonify
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token, create_refresh_token,
    get_jwt_identity, get_jwt
)
from datetime import datetime, timedelta, timezone

from app import app
from app import db
from app.config import Config
from app.utils import init_routing_func, check_request_data
from app.obj_utils import get_objs
from database.tables import User, Device  # , Game, TopScore, UserGame
import bcrypt

# memory_api, get, post = init_routing_func('memory_api', '/wmsdemoflask/')

'''
@get('/getgames')
def getGames():
    games = get_objs(Game)
    return jsonify(games), 200
'''

user, get, post = init_routing_func('user', '/api/user/')


@get('/login')
def get_login():
    return 405


@post('/login')
def post_login():
    data = request.json
    email = app.session.query(User).filter_by(email=data['email']).first()
    if email:
        user = email.__dict__
        storedHash = user['password']
        if bcrypt.checkpw(data['password'].encode('utf8'), storedHash):
            access_token = create_access_token(identity=user['email'])
            response = jsonify(access_token=access_token)
            response.headers['location'] = '/home'
            response.autocorrect_location_header = False
            response.headers.add('Access-Control-Allow-Origin', '*')
            return response, 201
        else:
            return jsonify(error="password incorrect"), 401
    else:
        return jsonify(error="user does not exist"), 401


@get('/register')
def get_register():
    return 405


@post('/register')
def post_register():
    data = request.json

    user = app.session.query(User).filter_by(username=data['username']).first()
    email = app.session.query(User).filter_by(email=data['email']).first()

    if user or email:
        # redirect to signin
        response = jsonify()
        response.status_code = 301
        response.headers['location'] = '/login'
        response.autocorrect_location_header = False
        return response

    new_user = User(email=data['email'],
                    username=data['username'],
                    password=bcrypt.hashpw(data['password'].encode('utf8'), bcrypt.gensalt()))
    app.session.add(new_user)
    app.session.flush()
    app.session.commit()

    access_token = create_access_token(identity=data['email'])
    response = jsonify(access_token=access_token)
    response.headers['location'] = '/home'
    response.autocorrect_location_header = False
    return response, 201


device, get, post = init_routing_func('device', '/api/device/')


@post('/new')
def post_device():
    data = request.json

    new_device = Device(name=data['name'],
                        description=data['description'],
                        ws_protocol=data['ws_protocol'],
                        ws_address=data['ws_address'])
    app.session.add(new_device)
    app.session.flush()
    app.session.commit()

    return jsonify(), 200
