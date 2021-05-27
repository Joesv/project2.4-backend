from flask import Flask, request, jsonify
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token, create_refresh_token,
    get_jwt_identity, get_jwt
)
from datetime import datetime, timedelta, timezone

from app import app
from app.utils import init_routing_func, check_request_data
from app.obj_utils import get_objs
from database.tables import User, Game, TopScore, UserGame

memory_api, get, post = init_routing_func('memory_api', '/wmsdemoflask/')

@get('/getgames')
def getGames():
    games = get_objs(Game)
    return jsonify(games), 200

user, get, post = init_routing_func('user', '/api/')
@get('/users')
def getUsers():
    users = get_objs(User)
    return jsonify(users), 200