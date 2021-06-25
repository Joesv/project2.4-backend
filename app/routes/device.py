from app.utils import init_routing_func
from app.weather import Weather
from database.tables import WeatherCard
from app import app
from flask import jsonify
from flask_jwt_extended import verify_jwt_in_request, get_jwt_identity

device, get, post, put, delete = init_routing_func('device', '/api/device/')


@get('/weathercards')
def get_all_cards():
    verify_jwt_in_request()
    user_id = get_jwt_identity()

    cards = app.session.query(WeatherCard).filter(WeatherCard.user_id == user_id).all()

    return jsonify(weatherCards=[card.to_dict() for card in cards]), 200


@get('/weather/<int:id>')
def get_weather(card_id):
    # get these from the db
    verify_jwt_in_request()

    user_id = get_jwt_identity()

    weather_card = app.session.query(WeatherCard).filter(
        WeatherCard.user_id == user_id,
        WeatherCard.id == card_id
    ).first()

    lat = weather_card.lat
    lon = weather_card.lon
    weather = Weather()
    return weather.get_weather_by_coords(lat, lon)
