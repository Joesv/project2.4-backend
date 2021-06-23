import datetime

import requests
import json
from app import app
from app.config import Config
from database.tables import WeatherCache
from sqlalchemy import desc


class Weather:
    apiKey = Config.OPENWEATHERAPIKEY
    baseUrl = 'https://api.openweathermap.org/data/2.5/weather?'
    oneCallBaseUrl = 'https://api.openweathermap.org/data/2.5/onecall?'
    units = 'metric'

    def normalize(self, number):
        return round(number, 1)

    def get_weather_by_coords(self, lat, lon):
        if not Config.ENABLEWEATHERAPI:
            return json.loads(Weather.default)

        lat = str(self.normalize(lat))
        lon = str(self.normalize(lon))

        deltaT = datetime.datetime.utcnow() - datetime.timedelta(minutes=15)
        cache = app.session.query(WeatherCache).filter(
            WeatherCache.lat == lat,
            WeatherCache.lon == lon,
            WeatherCache.timestamp >= deltaT
        ).first()

        if cache is None:
            print("not hitting the cache")
            url = f'{self.oneCallBaseUrl}lat={lat}&lon={lon}&units={self.units}&appid={self.apiKey}'
            resp = requests.get(url)
            # print(resp.json())
            json = resp.json()
            new_cache = WeatherCache(lat=lat, lon=lon, data=json)
            app.session.add(new_cache)
            app.session.flush()
            app.session.commit()

            return resp.json()
        print("hitting the cache")
        return cache.data

    default = """
    {
    "current": {
        "clouds": 90,
        "dew_point": 11.74,
        "dt": 1624226301,
        "feels_like": 13.92,
        "humidity": 85,
        "pressure": 1010,
        "sunrise": 1624158577,
        "sunset": 1624219691,
        "temp": 14.22,
        "uvi": 0,
        "visibility": 10000,
        "weather": [
            {
                "description": "overcast clouds",
                "icon": "04n",
                "id": 804,
                "main": "Clouds"
            }
        ],
        "wind_deg": 10,
        "wind_speed": 4.63
    },
    "daily": [
        {
            "clouds": 99,
            "dew_point": 12.31,
            "dt": 1624186800,
            "feels_like": {
                "day": 15.43,
                "eve": 13.95,
                "morn": 14.65,
                "night": 13.54
            },
            "humidity": 80,
            "moon_phase": 0.33,
            "moonrise": 1624199520,
            "moonset": 1624149900,
            "pop": 1,
            "pressure": 1009,
            "rain": 13.86,
            "sunrise": 1624158577,
            "sunset": 1624219691,
            "temp": {
                "day": 15.71,
                "eve": 14.37,
                "max": 16.05,
                "min": 13.42,
                "morn": 14.58,
                "night": 13.9
            },
            "uvi": 5.71,
            "weather": [
                {
                    "description": "heavy intensity rain",
                    "icon": "10d",
                    "id": 502,
                    "main": "Rain"
                }
            ],
            "wind_deg": 60,
            "wind_gust": 13.71,
            "wind_speed": 8.31
        },
        {
            "clouds": 100,
            "dew_point": 10.51,
            "dt": 1624273200,
            "feels_like": {
                "day": 12.36,
                "eve": 12.53,
                "morn": 12.55,
                "night": 11.59
            },
            "humidity": 86,
            "moon_phase": 0.37,
            "moonrise": 1624291320,
            "moonset": 1624237320,
            "pop": 0.79,
            "pressure": 1012,
            "rain": 1.58,
            "sunrise": 1624244988,
            "sunset": 1624306104,
            "temp": {
                "day": 12.78,
                "eve": 13.03,
                "max": 14.22,
                "min": 12.1,
                "morn": 13.12,
                "night": 12.1
            },
            "uvi": 1.31,
            "weather": [
                {
                    "description": "light rain",
                    "icon": "10d",
                    "id": 500,
                    "main": "Rain"
                }
            ],
            "wind_deg": 33,
            "wind_gust": 9.78,
            "wind_speed": 7.29
        },
        {
            "clouds": 86,
            "dew_point": 8.98,
            "dt": 1624359600,
            "feels_like": {
                "day": 14.18,
                "eve": 13.42,
                "morn": 12.16,
                "night": 11.47
            },
            "humidity": 68,
            "moon_phase": 0.41,
            "moonrise": 1624383300,
            "moonset": 1624324920,
            "pop": 0,
            "pressure": 1019,
            "sunrise": 1624331402,
            "sunset": 1624392515,
            "temp": {
                "day": 14.86,
                "eve": 14.05,
                "max": 15.04,
                "min": 11.6,
                "morn": 12.81,
                "night": 12.14
            },
            "uvi": 6.41,
            "weather": [
                {
                    "description": "overcast clouds",
                    "icon": "04d",
                    "id": 804,
                    "main": "Clouds"
                }
            ],
            "wind_deg": 26,
            "wind_gust": 7.9,
            "wind_speed": 7.05
        },
        {
            "clouds": 91,
            "dew_point": 11.61,
            "dt": 1624446000,
            "feels_like": {
                "day": 15.57,
                "eve": 14.59,
                "morn": 12.42,
                "night": 12.31
            },
            "humidity": 75,
            "moon_phase": 0.45,
            "moonrise": 1624475100,
            "moonset": 1624412940,
            "pop": 0.03,
            "pressure": 1022,
            "sunrise": 1624417819,
            "sunset": 1624478922,
            "temp": {
                "day": 15.96,
                "eve": 14.86,
                "max": 16.15,
                "min": 11.78,
                "morn": 13,
                "night": 12.66
            },
            "uvi": 4.8,
            "weather": [
                {
                    "description": "overcast clouds",
                    "icon": "04d",
                    "id": 804,
                    "main": "Clouds"
                }
            ],
            "wind_deg": 21,
            "wind_gust": 7.85,
            "wind_speed": 5.19
        },
        {
            "clouds": 21,
            "dew_point": 9.27,
            "dt": 1624532400,
            "feels_like": {
                "day": 15.99,
                "eve": 14.46,
                "morn": 13.94,
                "night": 11.19
            },
            "humidity": 62,
            "moon_phase": 0.5,
            "moonrise": 1624566240,
            "moonset": 1624501620,
            "pop": 0,
            "pressure": 1021,
            "sunrise": 1624504240,
            "sunset": 1624565326,
            "temp": {
                "day": 16.65,
                "eve": 15.14,
                "max": 16.65,
                "min": 11.83,
                "morn": 14.5,
                "night": 12.1
            },
            "uvi": 6.86,
            "weather": [
                {
                    "description": "few clouds",
                    "icon": "02d",
                    "id": 801,
                    "main": "Clouds"
                }
            ],
            "wind_deg": 12,
            "wind_gust": 4.21,
            "wind_speed": 3.66
        },
        {
            "clouds": 2,
            "dew_point": 6.75,
            "dt": 1624618800,
            "feels_like": {
                "day": 17.96,
                "eve": 16.11,
                "morn": 11.77,
                "night": 12.03
            },
            "humidity": 46,
            "moon_phase": 0.52,
            "moonrise": 1624656420,
            "moonset": 1624591320,
            "pop": 0,
            "pressure": 1018,
            "sunrise": 1624590663,
            "sunset": 1624651726,
            "temp": {
                "day": 18.82,
                "eve": 16.78,
                "max": 18.82,
                "min": 9.25,
                "morn": 12.77,
                "night": 13.1
            },
            "uvi": 6.72,
            "weather": [
                {
                    "description": "clear sky",
                    "icon": "01d",
                    "id": 800,
                    "main": "Clear"
                }
            ],
            "wind_deg": 7,
            "wind_gust": 2.56,
            "wind_speed": 2.47
        },
        {
            "clouds": 89,
            "dew_point": 11.55,
            "dt": 1624705200,
            "feels_like": {
                "day": 18.98,
                "eve": 17.28,
                "morn": 13.83,
                "night": 14.41
            },
            "humidity": 61,
            "moon_phase": 0.56,
            "moonrise": 0,
            "moonset": 1624681920,
            "pop": 0,
            "pressure": 1021,
            "sunrise": 1624677090,
            "sunset": 1624738123,
            "temp": {
                "day": 19.39,
                "eve": 17.44,
                "max": 19.54,
                "min": 11.57,
                "morn": 14.69,
                "night": 14.64
            },
            "uvi": 7,
            "weather": [
                {
                    "description": "overcast clouds",
                    "icon": "04d",
                    "id": 804,
                    "main": "Clouds"
                }
            ],
            "wind_deg": 31,
            "wind_gust": 5.37,
            "wind_speed": 3.85
        },
        {
            "clouds": 4,
            "dew_point": 14.85,
            "dt": 1624791600,
            "feels_like": {
                "day": 20.91,
                "eve": 18.47,
                "morn": 15.93,
                "night": 14.82
            },
            "humidity": 69,
            "moon_phase": 0.6,
            "moonrise": 1624745400,
            "moonset": 1624773240,
            "pop": 0,
            "pressure": 1019,
            "sunrise": 1624763520,
            "sunset": 1624824516,
            "temp": {
                "day": 20.96,
                "eve": 18.43,
                "max": 20.96,
                "min": 13.09,
                "morn": 16.19,
                "night": 14.95
            },
            "uvi": 7,
            "weather": [
                {
                    "description": "clear sky",
                    "icon": "01d",
                    "id": 800,
                    "main": "Clear"
                }
            ],
            "wind_deg": 49,
            "wind_gust": 8.41,
            "wind_speed": 5.54
        }
    ],
    "hourly": [
        {
            "clouds": 80,
            "dew_point": 11.24,
            "dt": 1624222800,
            "feels_like": 13.54,
            "humidity": 84,
            "pop": 0,
            "pressure": 1010,
            "temp": 13.9,
            "uvi": 0,
            "visibility": 10000,
            "weather": [
                {
                    "description": "broken clouds",
                    "icon": "04n",
                    "id": 803,
                    "main": "Clouds"
                }
            ],
            "wind_deg": 10,
            "wind_gust": 8.74,
            "wind_speed": 6.54
        },
        {
            "clouds": 90,
            "dew_point": 11.74,
            "dt": 1624226400,
            "feels_like": 13.92,
            "humidity": 85,
            "pop": 0,
            "pressure": 1010,
            "temp": 14.22,
            "uvi": 0,
            "visibility": 10000,
            "weather": [
                {
                    "description": "overcast clouds",
                    "icon": "04n",
                    "id": 804,
                    "main": "Clouds"
                }
            ],
            "wind_deg": 27,
            "wind_gust": 8.32,
            "wind_speed": 5.85
        },
        {
            "clouds": 85,
            "dew_point": 11.19,
            "dt": 1624230000,
            "feels_like": 13.47,
            "humidity": 84,
            "pop": 0,
            "pressure": 1010,
            "temp": 13.84,
            "uvi": 0,
            "visibility": 10000,
            "weather": [
                {
                    "description": "overcast clouds",
                    "icon": "04n",
                    "id": 804,
                    "main": "Clouds"
                }
            ],
            "wind_deg": 31,
            "wind_gust": 9.28,
            "wind_speed": 6.57
        },
        {
            "clouds": 82,
            "dew_point": 10.61,
            "dt": 1624233600,
            "feels_like": 13.01,
            "humidity": 83,
            "pop": 0,
            "pressure": 1010,
            "temp": 13.44,
            "uvi": 0,
            "visibility": 10000,
            "weather": [
                {
                    "description": "broken clouds",
                    "icon": "04n",
                    "id": 803,
                    "main": "Clouds"
                }
            ],
            "wind_deg": 33,
            "wind_gust": 9.37,
            "wind_speed": 6.58
        },
        {
            "clouds": 90,
            "dew_point": 10.05,
            "dt": 1624237200,
            "feels_like": 12.55,
            "humidity": 82,
            "pop": 0.01,
            "pressure": 1010,
            "temp": 13.05,
            "uvi": 0,
            "visibility": 10000,
            "weather": [
                {
                    "description": "overcast clouds",
                    "icon": "04n",
                    "id": 804,
                    "main": "Clouds"
                }
            ],
            "wind_deg": 43,
            "wind_gust": 9.63,
            "wind_speed": 6.58
        },
        {
            "clouds": 94,
            "dew_point": 9.66,
            "dt": 1624240800,
            "feels_like": 12.48,
            "humidity": 80,
            "pop": 0.01,
            "pressure": 1010,
            "temp": 13.03,
            "uvi": 0,
            "visibility": 10000,
            "weather": [
                {
                    "description": "overcast clouds",
                    "icon": "04n",
                    "id": 804,
                    "main": "Clouds"
                }
            ],
            "wind_deg": 44,
            "wind_gust": 8.57,
            "wind_speed": 6.05
        },
        {
            "clouds": 97,
            "dew_point": 9.08,
            "dt": 1624244400,
            "feels_like": 12.38,
            "humidity": 78,
            "pop": 0.04,
            "pressure": 1010,
            "temp": 12.99,
            "uvi": 0,
            "visibility": 10000,
            "weather": [
                {
                    "description": "overcast clouds",
                    "icon": "04n",
                    "id": 804,
                    "main": "Clouds"
                }
            ],
            "wind_deg": 47,
            "wind_gust": 8.22,
            "wind_speed": 5.8
        },
        {
            "clouds": 97,
            "dew_point": 9.26,
            "dt": 1624248000,
            "feels_like": 12.4,
            "humidity": 78,
            "pop": 0.09,
            "pressure": 1010,
            "temp": 13.01,
            "uvi": 0.06,
            "visibility": 10000,
            "weather": [
                {
                    "description": "overcast clouds",
                    "icon": "04d",
                    "id": 804,
                    "main": "Clouds"
                }
            ],
            "wind_deg": 45,
            "wind_gust": 8.45,
            "wind_speed": 6.09
        },
        {
            "clouds": 98,
            "dew_point": 9.6,
            "dt": 1624251600,
            "feels_like": 12.55,
            "humidity": 79,
            "pop": 0.17,
            "pressure": 1010,
            "temp": 13.12,
            "uvi": 0.21,
            "visibility": 10000,
            "weather": [
                {
                    "description": "overcast clouds",
                    "icon": "04d",
                    "id": 804,
                    "main": "Clouds"
                }
            ],
            "wind_deg": 40,
            "wind_gust": 8.8,
            "wind_speed": 6.51
        },
        {
            "clouds": 98,
            "dew_point": 9.68,
            "dt": 1624255200,
            "feels_like": 12.72,
            "humidity": 79,
            "pop": 0.24,
            "pressure": 1010,
            "temp": 13.27,
            "uvi": 0.55,
            "visibility": 10000,
            "weather": [
                {
                    "description": "overcast clouds",
                    "icon": "04d",
                    "id": 804,
                    "main": "Clouds"
                }
            ],
            "wind_deg": 34,
            "wind_gust": 8.58,
            "wind_speed": 6.51
        },
        {
            "clouds": 100,
            "dew_point": 9.9,
            "dt": 1624258800,
            "feels_like": 12.67,
            "humidity": 81,
            "pop": 0.48,
            "pressure": 1010,
            "temp": 13.18,
            "uvi": 0.53,
            "visibility": 10000,
            "weather": [
                {
                    "description": "overcast clouds",
                    "icon": "04d",
                    "id": 804,
                    "main": "Clouds"
                }
            ],
            "wind_deg": 31,
            "wind_gust": 9.13,
            "wind_speed": 7.05
        },
        {
            "clouds": 100,
            "dew_point": 10.18,
            "dt": 1624262400,
            "feels_like": 12.39,
            "humidity": 84,
            "pop": 0.52,
            "pressure": 1011,
            "rain": {
                "1h": 0.17
            },
            "temp": 12.86,
            "uvi": 0.9,
            "visibility": 10000,
            "weather": [
                {
                    "description": "light rain",
                    "icon": "10d",
                    "id": 500,
                    "main": "Rain"
                }
            ],
            "wind_deg": 31,
            "wind_gust": 9.02,
            "wind_speed": 6.56
        },
        {
            "clouds": 100,
            "dew_point": 10.1,
            "dt": 1624266000,
            "feels_like": 12.39,
            "humidity": 84,
            "pop": 0.66,
            "pressure": 1011,
            "rain": {
                "1h": 0.12
            },
            "temp": 12.86,
            "uvi": 1.31,
            "visibility": 10000,
            "weather": [
                {
                    "description": "light rain",
                    "icon": "10d",
                    "id": 500,
                    "main": "Rain"
                }
            ],
            "wind_deg": 27,
            "wind_gust": 9.22,
            "wind_speed": 6.73
        },
        {
            "clouds": 100,
            "dew_point": 10.33,
            "dt": 1624269600,
            "feels_like": 12.5,
            "humidity": 84,
            "pop": 0.66,
            "pressure": 1011,
            "temp": 12.96,
            "uvi": 0.93,
            "visibility": 10000,
            "weather": [
                {
                    "description": "overcast clouds",
                    "icon": "04d",
                    "id": 804,
                    "main": "Clouds"
                }
            ],
            "wind_deg": 33,
            "wind_gust": 9.78,
            "wind_speed": 7.29
        },
        {
            "clouds": 100,
            "dew_point": 10.51,
            "dt": 1624273200,
            "feels_like": 12.36,
            "humidity": 86,
            "pop": 0.7,
            "pressure": 1012,
            "rain": {
                "1h": 0.27
            },
            "temp": 12.78,
            "uvi": 1.05,
            "visibility": 10000,
            "weather": [
                {
                    "description": "light rain",
                    "icon": "10d",
                    "id": 500,
                    "main": "Rain"
                }
            ],
            "wind_deg": 33,
            "wind_gust": 9.2,
            "wind_speed": 6.69
        },
        {
            "clouds": 100,
            "dew_point": 10.7,
            "dt": 1624276800,
            "feels_like": 12.2,
            "humidity": 88,
            "pop": 0.75,
            "pressure": 1013,
            "rain": {
                "1h": 0.49
            },
            "temp": 12.59,
            "uvi": 1.07,
            "visibility": 10000,
            "weather": [
                {
                    "description": "light rain",
                    "icon": "10d",
                    "id": 500,
                    "main": "Rain"
                }
            ],
            "wind_deg": 30,
            "wind_gust": 7.8,
            "wind_speed": 5.45
        },
        {
            "clouds": 100,
            "dew_point": 10.65,
            "dt": 1624280400,
            "feels_like": 12.02,
            "humidity": 89,
            "pop": 0.79,
            "pressure": 1013,
            "rain": {
                "1h": 0.53
            },
            "temp": 12.4,
            "uvi": 0.92,
            "visibility": 10000,
            "weather": [
                {
                    "description": "light rain",
                    "icon": "10d",
                    "id": 500,
                    "main": "Rain"
                }
            ],
            "wind_deg": 27,
            "wind_gust": 8.79,
            "wind_speed": 6.3
        },
        {
            "clouds": 100,
            "dew_point": 10.31,
            "dt": 1624284000,
            "feels_like": 11.97,
            "humidity": 87,
            "pop": 0.67,
            "pressure": 1013,
            "temp": 12.4,
            "uvi": 0.75,
            "visibility": 10000,
            "weather": [
                {
                    "description": "overcast clouds",
                    "icon": "04d",
                    "id": 804,
                    "main": "Clouds"
                }
            ],
            "wind_deg": 31,
            "wind_gust": 8.62,
            "wind_speed": 5.97
        },
        {
            "clouds": 100,
            "dew_point": 10.06,
            "dt": 1624287600,
            "feels_like": 12.12,
            "humidity": 84,
            "pop": 0.63,
            "pressure": 1014,
            "temp": 12.61,
            "uvi": 0.53,
            "visibility": 10000,
            "weather": [
                {
                    "description": "overcast clouds",
                    "icon": "04d",
                    "id": 804,
                    "main": "Clouds"
                }
            ],
            "wind_deg": 33,
            "wind_gust": 8.04,
            "wind_speed": 5.51
        },
        {
            "clouds": 100,
            "dew_point": 10.04,
            "dt": 1624291200,
            "feels_like": 12.35,
            "humidity": 83,
            "pop": 0.55,
            "pressure": 1014,
            "temp": 12.84,
            "uvi": 0.95,
            "visibility": 10000,
            "weather": [
                {
                    "description": "overcast clouds",
                    "icon": "04d",
                    "id": 804,
                    "main": "Clouds"
                }
            ],
            "wind_deg": 34,
            "wind_gust": 8.24,
            "wind_speed": 5.47
        },
        {
            "clouds": 100,
            "dew_point": 10.11,
            "dt": 1624294800,
            "feels_like": 12.53,
            "humidity": 82,
            "pop": 0.51,
            "pressure": 1014,
            "temp": 13.03,
            "uvi": 0.49,
            "visibility": 10000,
            "weather": [
                {
                    "description": "overcast clouds",
                    "icon": "04d",
                    "id": 804,
                    "main": "Clouds"
                }
            ],
            "wind_deg": 33,
            "wind_gust": 8.07,
            "wind_speed": 5.43
        },
        {
            "clouds": 93,
            "dew_point": 10.24,
            "dt": 1624298400,
            "feels_like": 12.99,
            "humidity": 80,
            "pop": 0.5,
            "pressure": 1014,
            "temp": 13.5,
            "uvi": 0.21,
            "visibility": 10000,
            "weather": [
                {
                    "description": "overcast clouds",
                    "icon": "04d",
                    "id": 804,
                    "main": "Clouds"
                }
            ],
            "wind_deg": 25,
            "wind_gust": 7.81,
            "wind_speed": 5.43
        },
        {
            "clouds": 15,
            "dew_point": 9.89,
            "dt": 1624302000,
            "feels_like": 12.5,
            "humidity": 82,
            "pop": 0,
            "pressure": 1015,
            "temp": 13,
            "uvi": 0.15,
            "visibility": 10000,
            "weather": [
                {
                    "description": "few clouds",
                    "icon": "02d",
                    "id": 801,
                    "main": "Clouds"
                }
            ],
            "wind_deg": 23,
            "wind_gust": 7.2,
            "wind_speed": 4.82
        },
        {
            "clouds": 20,
            "dew_point": 9.57,
            "dt": 1624305600,
            "feels_like": 11.65,
            "humidity": 85,
            "pop": 0,
            "pressure": 1016,
            "temp": 12.16,
            "uvi": 0,
            "visibility": 10000,
            "weather": [
                {
                    "description": "few clouds",
                    "icon": "02d",
                    "id": 801,
                    "main": "Clouds"
                }
            ],
            "wind_deg": 22,
            "wind_gust": 6.98,
            "wind_speed": 4.45
        },
        {
            "clouds": 44,
            "dew_point": 9.54,
            "dt": 1624309200,
            "feels_like": 11.59,
            "humidity": 85,
            "pop": 0,
            "pressure": 1016,
            "temp": 12.1,
            "uvi": 0,
            "visibility": 10000,
            "weather": [
                {
                    "description": "scattered clouds",
                    "icon": "03n",
                    "id": 802,
                    "main": "Clouds"
                }
            ],
            "wind_deg": 21,
            "wind_gust": 7.63,
            "wind_speed": 4.92
        },
        {
            "clouds": 56,
            "dew_point": 8.99,
            "dt": 1624312800,
            "feels_like": 12.41,
            "humidity": 77,
            "pop": 0,
            "pressure": 1016,
            "temp": 13.04,
            "uvi": 0,
            "visibility": 10000,
            "weather": [
                {
                    "description": "broken clouds",
                    "icon": "04n",
                    "id": 803,
                    "main": "Clouds"
                }
            ],
            "wind_deg": 20,
            "wind_gust": 6.63,
            "wind_speed": 5.09
        },
        {
            "clouds": 64,
            "dew_point": 8.85,
            "dt": 1624316400,
            "feels_like": 12.69,
            "humidity": 75,
            "pop": 0,
            "pressure": 1016,
            "temp": 13.34,
            "uvi": 0,
            "visibility": 10000,
            "weather": [
                {
                    "description": "broken clouds",
                    "icon": "04n",
                    "id": 803,
                    "main": "Clouds"
                }
            ],
            "wind_deg": 17,
            "wind_gust": 6.78,
            "wind_speed": 5.25
        },
        {
            "clouds": 62,
            "dew_point": 8.91,
            "dt": 1624320000,
            "feels_like": 11.78,
            "humidity": 79,
            "pop": 0,
            "pressure": 1016,
            "temp": 12.42,
            "uvi": 0,
            "visibility": 10000,
            "weather": [
                {
                    "description": "broken clouds",
                    "icon": "04n",
                    "id": 803,
                    "main": "Clouds"
                }
            ],
            "wind_deg": 17,
            "wind_gust": 6.37,
            "wind_speed": 4.34
        },
        {
            "clouds": 23,
            "dew_point": 8.71,
            "dt": 1624323600,
            "feels_like": 11.39,
            "humidity": 80,
            "pop": 0,
            "pressure": 1016,
            "temp": 12.04,
            "uvi": 0,
            "visibility": 10000,
            "weather": [
                {
                    "description": "few clouds",
                    "icon": "02n",
                    "id": 801,
                    "main": "Clouds"
                }
            ],
            "wind_deg": 19,
            "wind_gust": 6.7,
            "wind_speed": 4.58
        },
        {
            "clouds": 23,
            "dew_point": 8.58,
            "dt": 1624327200,
            "feels_like": 11.01,
            "humidity": 82,
            "pop": 0,
            "pressure": 1017,
            "temp": 11.65,
            "uvi": 0,
            "visibility": 10000,
            "weather": [
                {
                    "description": "few clouds",
                    "icon": "02n",
                    "id": 801,
                    "main": "Clouds"
                }
            ],
            "wind_deg": 17,
            "wind_gust": 6.57,
            "wind_speed": 4.47
        },
        {
            "clouds": 48,
            "dew_point": 8.35,
            "dt": 1624330800,
            "feels_like": 10.93,
            "humidity": 81,
            "pop": 0,
            "pressure": 1017,
            "temp": 11.6,
            "uvi": 0,
            "visibility": 10000,
            "weather": [
                {
                    "description": "scattered clouds",
                    "icon": "03n",
                    "id": 802,
                    "main": "Clouds"
                }
            ],
            "wind_deg": 21,
            "wind_gust": 6.48,
            "wind_speed": 4.43
        },
        {
            "clouds": 61,
            "dew_point": 8.47,
            "dt": 1624334400,
            "feels_like": 11.22,
            "humidity": 80,
            "pop": 0,
            "pressure": 1017,
            "temp": 11.89,
            "uvi": 0.09,
            "visibility": 10000,
            "weather": [
                {
                    "description": "broken clouds",
                    "icon": "04d",
                    "id": 803,
                    "main": "Clouds"
                }
            ],
            "wind_deg": 19,
            "wind_gust": 7.15,
            "wind_speed": 4.61
        },
        {
            "clouds": 69,
            "dew_point": 8.91,
            "dt": 1624338000,
            "feels_like": 12.16,
            "humidity": 77,
            "pop": 0,
            "pressure": 1017,
            "temp": 12.81,
            "uvi": 0.33,
            "visibility": 10000,
            "weather": [
                {
                    "description": "broken clouds",
                    "icon": "04d",
                    "id": 803,
                    "main": "Clouds"
                }
            ],
            "wind_deg": 18,
            "wind_gust": 7.9,
            "wind_speed": 5.62
        },
        {
            "clouds": 74,
            "dew_point": 9.2,
            "dt": 1624341600,
            "feels_like": 12.85,
            "humidity": 75,
            "pop": 0,
            "pressure": 1018,
            "temp": 13.49,
            "uvi": 0.84,
            "visibility": 10000,
            "weather": [
                {
                    "description": "broken clouds",
                    "icon": "04d",
                    "id": 803,
                    "main": "Clouds"
                }
            ],
            "wind_deg": 26,
            "wind_gust": 7.09,
            "wind_speed": 5.61
        },
        {
            "clouds": 99,
            "dew_point": 9.07,
            "dt": 1624345200,
            "feels_like": 13.4,
            "humidity": 72,
            "pop": 0,
            "pressure": 1018,
            "temp": 14.06,
            "uvi": 1.75,
            "visibility": 10000,
            "weather": [
                {
                    "description": "overcast clouds",
                    "icon": "04d",
                    "id": 804,
                    "main": "Clouds"
                }
            ],
            "wind_deg": 26,
            "wind_gust": 6.73,
            "wind_speed": 6.08
        },
        {
            "clouds": 72,
            "dew_point": 9.09,
            "dt": 1624348800,
            "feels_like": 13.78,
            "humidity": 70,
            "pop": 0,
            "pressure": 1018,
            "temp": 14.45,
            "uvi": 2.97,
            "visibility": 10000,
            "weather": [
                {
                    "description": "broken clouds",
                    "icon": "04d",
                    "id": 803,
                    "main": "Clouds"
                }
            ],
            "wind_deg": 26,
            "wind_gust": 7.33,
            "wind_speed": 7.05
        },
        {
            "clouds": 77,
            "dew_point": 8.94,
            "dt": 1624352400,
            "feels_like": 13.92,
            "humidity": 69,
            "pop": 0,
            "pressure": 1018,
            "temp": 14.6,
            "uvi": 4.33,
            "visibility": 10000,
            "weather": [
                {
                    "description": "broken clouds",
                    "icon": "04d",
                    "id": 803,
                    "main": "Clouds"
                }
            ],
            "wind_deg": 27,
            "wind_gust": 6.76,
            "wind_speed": 6.54
        },
        {
            "clouds": 82,
            "dew_point": 8.94,
            "dt": 1624356000,
            "feels_like": 13.99,
            "humidity": 68,
            "pop": 0,
            "pressure": 1018,
            "temp": 14.69,
            "uvi": 5.57,
            "visibility": 10000,
            "weather": [
                {
                    "description": "broken clouds",
                    "icon": "04d",
                    "id": 803,
                    "main": "Clouds"
                }
            ],
            "wind_deg": 28,
            "wind_gust": 6.42,
            "wind_speed": 6.23
        },
        {
            "clouds": 86,
            "dew_point": 8.98,
            "dt": 1624359600,
            "feels_like": 14.18,
            "humidity": 68,
            "pop": 0,
            "pressure": 1019,
            "temp": 14.86,
            "uvi": 6.31,
            "visibility": 10000,
            "weather": [
                {
                    "description": "overcast clouds",
                    "icon": "04d",
                    "id": 804,
                    "main": "Clouds"
                }
            ],
            "wind_deg": 24,
            "wind_gust": 6.38,
            "wind_speed": 6.17
        },
        {
            "clouds": 81,
            "dew_point": 8.95,
            "dt": 1624363200,
            "feels_like": 14.35,
            "humidity": 67,
            "pop": 0,
            "pressure": 1019,
            "temp": 15.04,
            "uvi": 6.41,
            "visibility": 10000,
            "weather": [
                {
                    "description": "broken clouds",
                    "icon": "04d",
                    "id": 803,
                    "main": "Clouds"
                }
            ],
            "wind_deg": 24,
            "wind_gust": 6.33,
            "wind_speed": 6.09
        },
        {
            "clouds": 100,
            "dew_point": 8.84,
            "dt": 1624366800,
            "feels_like": 14.15,
            "humidity": 67,
            "pop": 0,
            "pressure": 1019,
            "temp": 14.86,
            "uvi": 6.09,
            "visibility": 10000,
            "weather": [
                {
                    "description": "overcast clouds",
                    "icon": "04d",
                    "id": 804,
                    "main": "Clouds"
                }
            ],
            "wind_deg": 26,
            "wind_gust": 6.28,
            "wind_speed": 5.95
        },
        {
            "clouds": 78,
            "dew_point": 9.02,
            "dt": 1624370400,
            "feels_like": 14.33,
            "humidity": 67,
            "pop": 0,
            "pressure": 1019,
            "temp": 15.02,
            "uvi": 4.93,
            "visibility": 10000,
            "weather": [
                {
                    "description": "broken clouds",
                    "icon": "04d",
                    "id": 803,
                    "main": "Clouds"
                }
            ],
            "wind_deg": 26,
            "wind_gust": 6.41,
            "wind_speed": 6.11
        },
        {
            "clouds": 74,
            "dew_point": 8.96,
            "dt": 1624374000,
            "feels_like": 14.17,
            "humidity": 68,
            "pop": 0,
            "pressure": 1019,
            "temp": 14.85,
            "uvi": 3.52,
            "visibility": 10000,
            "weather": [
                {
                    "description": "broken clouds",
                    "icon": "04d",
                    "id": 803,
                    "main": "Clouds"
                }
            ],
            "wind_deg": 28,
            "wind_gust": 5.83,
            "wind_speed": 5.66
        },
        {
            "clouds": 80,
            "dew_point": 8.84,
            "dt": 1624377600,
            "feels_like": 13.65,
            "humidity": 70,
            "pop": 0,
            "pressure": 1019,
            "temp": 14.33,
            "uvi": 2.06,
            "visibility": 10000,
            "weather": [
                {
                    "description": "broken clouds",
                    "icon": "04d",
                    "id": 803,
                    "main": "Clouds"
                }
            ],
            "wind_deg": 23,
            "wind_gust": 5.66,
            "wind_speed": 5.42
        },
        {
            "clouds": 84,
            "dew_point": 9.19,
            "dt": 1624381200,
            "feels_like": 13.42,
            "humidity": 73,
            "pop": 0,
            "pressure": 1019,
            "temp": 14.05,
            "uvi": 1.06,
            "visibility": 10000,
            "weather": [
                {
                    "description": "broken clouds",
                    "icon": "04d",
                    "id": 803,
                    "main": "Clouds"
                }
            ],
            "wind_deg": 21,
            "wind_gust": 6.32,
            "wind_speed": 5.45
        },
        {
            "clouds": 87,
            "dew_point": 9.32,
            "dt": 1624384800,
            "feels_like": 13.06,
            "humidity": 75,
            "pop": 0,
            "pressure": 1019,
            "temp": 13.68,
            "uvi": 0.44,
            "visibility": 10000,
            "weather": [
                {
                    "description": "overcast clouds",
                    "icon": "04d",
                    "id": 804,
                    "main": "Clouds"
                }
            ],
            "wind_deg": 22,
            "wind_gust": 7.41,
            "wind_speed": 5.97
        },
        {
            "clouds": 100,
            "dew_point": 9.02,
            "dt": 1624388400,
            "feels_like": 12.34,
            "humidity": 77,
            "pop": 0,
            "pressure": 1020,
            "temp": 12.98,
            "uvi": 0.14,
            "visibility": 10000,
            "weather": [
                {
                    "description": "overcast clouds",
                    "icon": "04d",
                    "id": 804,
                    "main": "Clouds"
                }
            ],
            "wind_deg": 26,
            "wind_gust": 7.76,
            "wind_speed": 5.44
        },
        {
            "clouds": 100,
            "dew_point": 8.64,
            "dt": 1624392000,
            "feels_like": 11.83,
            "humidity": 77,
            "pop": 0,
            "pressure": 1020,
            "temp": 12.51,
            "uvi": 0,
            "visibility": 10000,
            "weather": [
                {
                    "description": "overcast clouds",
                    "icon": "04d",
                    "id": 804,
                    "main": "Clouds"
                }
            ],
            "wind_deg": 25,
            "wind_gust": 7.9,
            "wind_speed": 5.26
        }
    ],
    "lat": 53.2192,
    "lon": 5.6667,
    "minutely": [
        {
            "dt": 1624226340,
            "precipitation": 0
        },
        {
            "dt": 1624226400,
            "precipitation": 0
        },
        {
            "dt": 1624226460,
            "precipitation": 0
        },
        {
            "dt": 1624226520,
            "precipitation": 0
        },
        {
            "dt": 1624226580,
            "precipitation": 0
        },
        {
            "dt": 1624226640,
            "precipitation": 0
        },
        {
            "dt": 1624226700,
            "precipitation": 0
        },
        {
            "dt": 1624226760,
            "precipitation": 0
        },
        {
            "dt": 1624226820,
            "precipitation": 0
        },
        {
            "dt": 1624226880,
            "precipitation": 0
        },
        {
            "dt": 1624226940,
            "precipitation": 0
        },
        {
            "dt": 1624227000,
            "precipitation": 0
        },
        {
            "dt": 1624227060,
            "precipitation": 0
        },
        {
            "dt": 1624227120,
            "precipitation": 0
        },
        {
            "dt": 1624227180,
            "precipitation": 0
        },
        {
            "dt": 1624227240,
            "precipitation": 0
        },
        {
            "dt": 1624227300,
            "precipitation": 0
        },
        {
            "dt": 1624227360,
            "precipitation": 0
        },
        {
            "dt": 1624227420,
            "precipitation": 0
        },
        {
            "dt": 1624227480,
            "precipitation": 0
        },
        {
            "dt": 1624227540,
            "precipitation": 0
        },
        {
            "dt": 1624227600,
            "precipitation": 0
        },
        {
            "dt": 1624227660,
            "precipitation": 0
        },
        {
            "dt": 1624227720,
            "precipitation": 0
        },
        {
            "dt": 1624227780,
            "precipitation": 0
        },
        {
            "dt": 1624227840,
            "precipitation": 0
        },
        {
            "dt": 1624227900,
            "precipitation": 0
        },
        {
            "dt": 1624227960,
            "precipitation": 0
        },
        {
            "dt": 1624228020,
            "precipitation": 0
        },
        {
            "dt": 1624228080,
            "precipitation": 0
        },
        {
            "dt": 1624228140,
            "precipitation": 0
        },
        {
            "dt": 1624228200,
            "precipitation": 0
        },
        {
            "dt": 1624228260,
            "precipitation": 0
        },
        {
            "dt": 1624228320,
            "precipitation": 0
        },
        {
            "dt": 1624228380,
            "precipitation": 0
        },
        {
            "dt": 1624228440,
            "precipitation": 0
        },
        {
            "dt": 1624228500,
            "precipitation": 0
        },
        {
            "dt": 1624228560,
            "precipitation": 0
        },
        {
            "dt": 1624228620,
            "precipitation": 0
        },
        {
            "dt": 1624228680,
            "precipitation": 0
        },
        {
            "dt": 1624228740,
            "precipitation": 0
        },
        {
            "dt": 1624228800,
            "precipitation": 0
        },
        {
            "dt": 1624228860,
            "precipitation": 0
        },
        {
            "dt": 1624228920,
            "precipitation": 0
        },
        {
            "dt": 1624228980,
            "precipitation": 0
        },
        {
            "dt": 1624229040,
            "precipitation": 0
        },
        {
            "dt": 1624229100,
            "precipitation": 0
        },
        {
            "dt": 1624229160,
            "precipitation": 0
        },
        {
            "dt": 1624229220,
            "precipitation": 0
        },
        {
            "dt": 1624229280,
            "precipitation": 0
        },
        {
            "dt": 1624229340,
            "precipitation": 0
        },
        {
            "dt": 1624229400,
            "precipitation": 0
        },
        {
            "dt": 1624229460,
            "precipitation": 0
        },
        {
            "dt": 1624229520,
            "precipitation": 0
        },
        {
            "dt": 1624229580,
            "precipitation": 0
        },
        {
            "dt": 1624229640,
            "precipitation": 0
        },
        {
            "dt": 1624229700,
            "precipitation": 0
        },
        {
            "dt": 1624229760,
            "precipitation": 0
        },
        {
            "dt": 1624229820,
            "precipitation": 0
        },
        {
            "dt": 1624229880,
            "precipitation": 0
        },
        {
            "dt": 1624229940,
            "precipitation": 0
        }
    ],
    "timezone": "Europe/Amsterdam",
    "timezone_offset": 7200
}"""
