from flask import request, jsonify
from flask_jwt_extended import verify_jwt_in_request, get_jwt_identity

from app import app
from app.utils import init_routing_func
from database.tables import DummyDevice

dummy_device, get, post, put, delete = init_routing_func('dummy_device', '/api/dummy_device/')


@post('/')
def post_dummy_device():
    # print("hello")
    verify_jwt_in_request()
    data = request.json

    # user = app.session.query(User).filter(User.id == get_jwt_identity()).first()
    user_id = get_jwt_identity()

    new_device = DummyDevice(dummy_type=data['dummy_type'],
                             name=data['name'],
                             user_id=user_id,
                             description=data['description'],
                             value=0)
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


@delete('/<int:device_id>')
def delete_dummy_device(device_id):
    verify_jwt_in_request()

    device = app.session.query(DummyDevice).filter(DummyDevice.id == device_id).first()
    user_id = get_jwt_identity()
    if device.user_id != user_id:
        return jsonify(), 403

    app.session.delete(device)
    app.session.commit()

    return jsonify(), 200


@put('/<int:device_id>')
def update_dummy_device(device_id):
    verify_jwt_in_request()

    device = app.session.query(DummyDevice).filter(DummyDevice.id == device_id).first()
    user_id = get_jwt_identity()
    if device.user_id != user_id:
        return jsonify(), 403

    data = request.json
    # is_on = data['status']
    # print(is_on)

    # update database
    device.value = data['status']
    app.session.commit()

    return jsonify(), 200
