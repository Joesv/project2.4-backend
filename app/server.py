from flask import Flask, request, jsonify
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token, create_refresh_token,
    get_jwt_identity, get_jwt, verify_jwt_in_request
)
from datetime import datetime, timedelta, timezone

from app import app
from app import db
from app.config import Config
from app.utils import init_routing_func, check_request_data
from app.obj_utils import get_objs
from app.weather import Weather
from database.tables import User, LampDevice  # , Game, TopScore, UserGame
import bcrypt

# memory_api, get, post = init_routing_func('memory_api', '/wmsdemoflask/')

'''
@get('/getgames')
def getGames():
    games = get_objs(Game)
    return jsonify(games), 200
'''

user, get, post, put, delete = init_routing_func('user', '/api/user/')


@get('/login')
def get_login():
    return 405


@post('/login')
def post_login():
    data = request.json
    loggedin_user = app.session.query(User).filter_by(email=data['email']).first()
    if loggedin_user:
        if bcrypt.checkpw(data['password'].encode('utf8'), loggedin_user.password):
            access_token = create_access_token(identity=loggedin_user.id)
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

    user_id = new_user.id
    print(f"Registered user id is {user_id}")

    access_token = create_access_token(identity=user_id)
    response = jsonify(access_token=access_token)
    response.headers['location'] = '/home'
    response.autocorrect_location_header = False
    return response, 201


lamp_device, get, post, put, delete = init_routing_func('lamp_device', '/api/lamp_device/')


@post('/')
def post_lamp_device():
    verify_jwt_in_request()
    data = request.json

    # user = app.session.query(User).filter(User.id == get_jwt_identity()).first()
    user_id = get_jwt_identity()

    new_lamp = LampDevice(name=data['name'],
                          user_id=user_id,
                          description=data['description'],
                          on_url=data['on_url'],
                          off_url=data['off_url'])
    app.session.add(new_lamp)
    app.session.flush()
    app.session.commit()

    return jsonify(), 201


@get('/')
def get_lamp_devices():
    verify_jwt_in_request()

    user_id = get_jwt_identity()
    # user = app.session.query(User).filter(User.id == user_id).first()
    # lamps = user.lamp_devices.all()
    lamps = app.session.query(LampDevice).filter(LampDevice.user_id == user_id).all()

    return jsonify(lamps=[l.to_dict() for l in lamps]), 200


device, get, post, put, delete = init_routing_func('device', '/api/device/')


@get('/weather')
def get_weather():
    #get these from the db
    lat = 53.21917
    lon = 5.6667
    return Weather.get_weather_by_coords(lat, lon)
