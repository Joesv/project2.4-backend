from flask import jsonify, request
from flask_jwt_extended import verify_jwt_in_request, get_jwt_identity

from app import app
from app.utils import init_routing_func
from app.weather import Weather
from database.tables import WeatherCard

device, get, post, put, delete = init_routing_func('device', '/api/device/')


@get('/weathercards')
def get_all_cards():
    verify_jwt_in_request()
    user_id = get_jwt_identity()

    cards = app.session.query(WeatherCard).filter(WeatherCard.user_id == user_id).all()

    return jsonify(weatherCards=[card.to_dict() for card in cards]), 200


@get('/weather/<int:id>')
def get_weather(id):
    # get these from the db
    verify_jwt_in_request()

    user_id = get_jwt_identity()

    weather_card = app.session.query(WeatherCard).filter(
        WeatherCard.user_id == user_id,
        WeatherCard.id == id
    ).first()

    lat = weather_card.lat
    lon = weather_card.lon
    weather = Weather()
    return weather.get_weather_by_coords(lat, lon)


@post('/weathercard')
def new_weather():
    verify_jwt_in_request()
    user_id = get_jwt_identity()

    data = request.json

    weather = Weather()
    lat = data['lat']
    lon = data['lon']

    location = weather.get_location(lat, lon)
    print(location)

    new_weather_card = WeatherCard(
        name=data['name'],
        user_id=user_id,
        lat=data['lat'],
        lon=data['lon'],
        locationname=location
    )
    app.session.add(new_weather_card)
    app.session.flush()
    app.session.commit()

    return jsonify(), 201


@delete('/weathercard/<int:device_id>')
def delete_weathercard(device_id):
    verify_jwt_in_request()
    card = app.session.query(WeatherCard).filter(WeatherCard.id == device_id).first()
    user_id = get_jwt_identity()
    if device_id != user_id:
        return jsonify(), 301

    app.session.delete(device)
    app.session.commit()
    return jsonify(), 200
