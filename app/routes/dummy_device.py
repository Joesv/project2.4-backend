from flask import request, jsonify
from flask_jwt_extended import verify_jwt_in_request, get_jwt_identity

from app import app
from app.utils import init_routing_func
from database.tables import DummyDevice

dummy_device, get, post, put, delete = init_routing_func('dummy_device', '/api/dummy_device/')


@post('/')
def post_dummy_device():
    #print("hello")
    verify_jwt_in_request()
    data = request.json

    # user = app.session.query(User).filter(User.id == get_jwt_identity()).first()
    user_id = get_jwt_identity()

    new_device = DummyDevice(dummy_type=data['dummy_type'],
                          name=data['name'],
                          user_id=user_id,
                          description=data['description'],
                          value=1)
    app.session.add(new_device)
    app.session.flush()
    app.session.commit()

    return jsonify(), 201

@get('/')
def get_dummy_devices():
    verify_jwt_in_request()

    user_id = get_jwt_identity()
    dummys = app.session.query(DummyDevice).filter(DummyDevice.user_id == user_id).all()

    return jsonify(dummys=[d.to_dict() for d in dummys]), 200
