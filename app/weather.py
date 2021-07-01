import datetime

import requests
from sqlalchemy import desc

from app import app
from app.config import Config
from database.tables import WeatherCache


class Weather:
    apiKey = Config.OPENWEATHERAPIKEY
    baseUrl = 'https://api.openweathermap.org/data/2.5/weather?'
    oneCallBaseUrl = 'https://api.openweathermap.org/data/2.5/onecall?'
    reverseBaseUrl = 'http://api.openweathermap.org/geo/1.0/reverse?'
    units = 'metric'

    def normalize(self, number):
        return round(number, 1)

    def get_weather_by_coords(self, lat, lon):
        lat = str(self.normalize(lat))
        lon = str(self.normalize(lon))

        deltaT = datetime.datetime.utcnow() - datetime.timedelta(minutes=15)
        cache = app.session.query(WeatherCache).filter(
            WeatherCache.lat == lat,
            WeatherCache.lon == lon,
            WeatherCache.timestamp >= deltaT
        ).order_by(desc(WeatherCache.timestamp)).first()

        if cache is None:  # cache doesnt return anything
            self.delete_old(lat, lon)
            url = f'{self.oneCallBaseUrl}lat={lat}&lon={lon}&units={self.units}&appid={self.apiKey}'
            resp = requests.get(url)
            json = resp.json()
            new_cache = WeatherCache(lat=lat, lon=lon, data=json)
            app.session.add(new_cache)
            app.session.flush()
            app.session.commit()

            return resp.json()
        # return from cache
        return cache.data

    def get_location(self, lat, lon):
        limit = 1
        url = f'{self.reverseBaseUrl}lat={lat}&lon={lon}&limit={limit}&appid={self.apiKey}'
        resp = requests.get(url)
        json = resp.json()
        print(json)
        location = json[0]['name']
        return location

    def delete_old(self, lat, lon):
        deltaT = datetime.datetime.utcnow() - datetime.timedelta(minutes=15)
        cache = app.session.query(WeatherCache).filter(
            WeatherCache.lat == lat,
            WeatherCache.lon == lon,
            WeatherCache.timestamp < deltaT
        ).order_by(desc(WeatherCache.timestamp)).first() #find the older one
        if cache is not None:
            app.session.delete(cache)
            app.session.flush()
            app.session.commit()


