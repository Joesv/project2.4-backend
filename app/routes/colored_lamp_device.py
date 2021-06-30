from flask import request, jsonify
from flask_jwt_extended import verify_jwt_in_request, get_jwt_identity

from app import app
from app.utils import init_routing_func
from database.tables import User, ColoredLampDevice
import requests

colored_lamp_device, get, post, put, delete = init_routing_func('colored_lamp_device', '/api/colored_lamp_device/')


@post('/')
def post_colored_lamp_device():
    verify_jwt_in_request()
    data = request.json

    user_id = get_jwt_identity()

    new_lamp = ColoredLampDevice(name=data['name'],
                                 user_id=user_id,
                                 description=data['description'],
                                 update_url=data['update_url'])
    app.session.add(new_lamp)
    app.session.flush()
    app.session.commit()

    return jsonify(), 201


@get('/')
def get_colored_lamp_devices():
    verify_jwt_in_request()

    user_id = get_jwt_identity()
    user = app.session.query(User).filter(User.id == user_id).first()
    lamps = user.colored_lamp_devices

    return jsonify(colored_lamps=[cl.to_dict() for cl in lamps]), 200


@delete('/<int:device_id>')
def delete_colored_lamp_device(device_id):
    verify_jwt_in_request()

    device = app.session.query(ColoredLampDevice).filter(ColoredLampDevice.id == device_id).first()
    user_id = get_jwt_identity()
    if device.user_id != user_id:
        return jsonify(), 403

    app.session.delete(device)
    app.session.commit()

    return jsonify(), 200


@put('/<int:device_id>')
def update_colored_lamp_device(device_id):
    verify_jwt_in_request()

    device = app.session.query(ColoredLampDevice).filter(ColoredLampDevice.id == device_id).first()
    user_id = get_jwt_identity()
    if device.user_id != user_id:
        return jsonify(), 403

    data = request.json
    red = data['red']
    green = data['green']
    blue = data['blue']

    # update lamp
    device_update_url = device.update_url \
        .replace('{red}', str(red / 255)) \
        .replace('{green}', str(green / 255)) \
        .replace('{blue}', str(blue / 255))

    print(f'{device_update_url}')

    response = requests.get(device_update_url)
    if response.status_code != 200:
        return jsonify(), 500

    # update database
    device.last_red = red
    device.last_green = green
    device.last_blue = blue
    app.session.commit()

    return jsonify(), 200
