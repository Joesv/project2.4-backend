from flask import request, jsonify
from flask_jwt_extended import verify_jwt_in_request, get_jwt_identity

from app import app
from app.utils import init_routing_func
from database.tables import LampDevice, User

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
    user = app.session.query(User).filter(User.id == user_id).first()
    lamps = user.lamp_devices

    return jsonify(lamps=[l.to_dict() for l in lamps]), 200


@delete('/<int:device_id>')
def delete_lamp_device(device_id):
    verify_jwt_in_request()

    user_id = get_jwt_identity()
    device = app.session.query(LampDevice).filter(LampDevice.user_id == user_id).first()
    if not device:
        return jsonify(), 404

    app.session.delete(device)
    app.session.commit()

    return jsonify(), 200
