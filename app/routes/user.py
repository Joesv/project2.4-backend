import bcrypt
from flask import request, jsonify
from flask_jwt_extended import create_access_token

from app import app
from app.utils import init_routing_func
from database.tables import User

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
            return jsonify(error="email or password is incorrect"), 401
    else:
        return jsonify(error="email or password is incorrect"), 401


@get('/register')
def get_register():
    return 405


@post('/register')
def post_register():
    data = request.json

    user = app.session.query(User).filter_by(username=data['username']).first()
    email = app.session.query(User).filter_by(email=data['email']).first()

    error = ""
    if user:
        error = "Username already in use. "
    if email:
        error = "Email already in use."
    if error != "":
        response = jsonify(error=error), 301
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
