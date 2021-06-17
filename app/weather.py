import requests
import json
from app import app
from app.config import Config


class Weather:
    apiKey = Config.OPENWEATHERAPIKEY
    baseUrl = 'https://api.openweathermap.org/data/2.5/weather?'
    oneCallBaseUrl = 'https://api.openweathermap.org/data/2.5/onecall?'

    def get_weather_by_coords(lat, lon):
        if not Config.ENABLEWEATHERAPI:
            return json.loads(Weather.default)

        url = f'{Weather.oneCallBaseUrl}lat={lat}&lon={lon}&units=metric&appid={Weather.apiKey}'
        resp = requests.get(url)
        # print(resp.json())
        return resp.json()



    default = """
    {
  "current": {
    "clouds": 39, 
    "dew_point": 291.94, 
    "dt": 1623949479, 
    "feels_like": 301.24, 
    "humidity": 61, 
    "pressure": 1011, 
    "sunrise": 1623899149, 
    "sunset": 1623960213, 
    "temp": 300.1, 
    "uvi": 1.04, 
    "visibility": 10000, 
    "weather": [
      {
        "description": "scattered clouds", 
        "icon": "03d", 
        "id": 802, 
        "main": "Clouds"
      }
    ], 
    "wind_deg": 270, 
    "wind_speed": 5.14
  }, 
  "daily": [
    {
      "clouds": 8, 
      "dew_point": 292.51, 
      "dt": 1623927600, 
      "feels_like": {
        "day": 303.91, 
        "eve": 301.24, 
        "morn": 293.73, 
        "night": 292.62
      }, 
      "humidity": 55, 
      "moon_phase": 0.22, 
      "moonrise": 1623925080, 
      "moonset": 1623887880, 
      "pop": 0.78, 
      "pressure": 1010, 
      "rain": 1.28, 
      "sunrise": 1623899149, 
      "sunset": 1623960213, 
      "temp": {
        "day": 302.45, 
        "eve": 300.1, 
        "max": 302.99, 
        "min": 290.64, 
        "morn": 293.4, 
        "night": 292.32
      }, 
      "uvi": 6.5, 
      "weather": [
        {
          "description": "light rain", 
          "icon": "10d", 
          "id": 500, 
          "main": "Rain"
        }
      ], 
      "wind_deg": 189, 
      "wind_gust": 8.92, 
      "wind_speed": 6.28
    }, 
    {
      "clouds": 100, 
      "dew_point": 292.22, 
      "dt": 1624014000, 
      "feels_like": {
        "day": 296.8, 
        "eve": 302.58, 
        "morn": 291.36, 
        "night": 295.02
      }, 
      "humidity": 77, 
      "moon_phase": 0.25, 
      "moonrise": 1624016400, 
      "moonset": 1623975180, 
      "pop": 1, 
      "pressure": 1013, 
      "rain": 5.35, 
      "sunrise": 1623985550, 
      "sunset": 1624046637, 
      "temp": {
        "day": 296.41, 
        "eve": 300.54, 
        "max": 300.54, 
        "min": 289.78, 
        "morn": 291.11, 
        "night": 294.65
      }, 
      "uvi": 4.82, 
      "weather": [
        {
          "description": "light rain", 
          "icon": "10d", 
          "id": 500, 
          "main": "Rain"
        }
      ], 
      "wind_deg": 219, 
      "wind_gust": 11.9, 
      "wind_speed": 4.71
    }, 
    {
      "clouds": 65, 
      "dew_point": 284.61, 
      "dt": 1624100400, 
      "feels_like": {
        "day": 290.21, 
        "eve": 288.33, 
        "morn": 287.68, 
        "night": 284.2
      }, 
      "humidity": 68, 
      "moon_phase": 0.29, 
      "moonrise": 1624107780, 
      "moonset": 1624062420, 
      "pop": 0.69, 
      "pressure": 1017, 
      "sunrise": 1624071954, 
      "sunset": 1624133057, 
      "temp": {
        "day": 290.63, 
        "eve": 288.76, 
        "max": 293.67, 
        "min": 284.67, 
        "morn": 287.9, 
        "night": 284.67
      }, 
      "uvi": 3.68, 
      "weather": [
        {
          "description": "broken clouds", 
          "icon": "04d", 
          "id": 803, 
          "main": "Clouds"
        }
      ], 
      "wind_deg": 210, 
      "wind_gust": 17.03, 
      "wind_speed": 9.72
    }, 
    {
      "clouds": 98, 
      "dew_point": 290.98, 
      "dt": 1624186800, 
      "feels_like": {
        "day": 296.04, 
        "eve": 294.53, 
        "morn": 285.59, 
        "night": 288.33
      }, 
      "humidity": 74, 
      "moon_phase": 0.33, 
      "moonrise": 1624199340, 
      "moonset": 1624149660, 
      "pop": 0.92, 
      "pressure": 1006, 
      "rain": 2.09, 
      "sunrise": 1624158361, 
      "sunset": 1624219475, 
      "temp": {
        "day": 295.79, 
        "eve": 294.27, 
        "max": 296.1, 
        "min": 284.44, 
        "morn": 285.81, 
        "night": 288.28
      }, 
      "uvi": 5.16, 
      "weather": [
        {
          "description": "light rain", 
          "icon": "10d", 
          "id": 500, 
          "main": "Rain"
        }
      ], 
      "wind_deg": 73, 
      "wind_gust": 18.34, 
      "wind_speed": 9.05
    }, 
    {
      "clouds": 77, 
      "dew_point": 287.11, 
      "dt": 1624273200, 
      "feels_like": {
        "day": 293.22, 
        "eve": 286.22, 
        "morn": 287.37, 
        "night": 284.23
      }, 
      "humidity": 67, 
      "moon_phase": 0.37, 
      "moonrise": 1624291140, 
      "moonset": 1624237080, 
      "pop": 0.46, 
      "pressure": 1007, 
      "rain": 0.53, 
      "sunrise": 1624244772, 
      "sunset": 1624305888, 
      "temp": {
        "day": 293.39, 
        "eve": 286.48, 
        "max": 293.39, 
        "min": 284.55, 
        "morn": 287.72, 
        "night": 284.55
      }, 
      "uvi": 6.22, 
      "weather": [
        {
          "description": "light rain", 
          "icon": "10d", 
          "id": 500, 
          "main": "Rain"
        }
      ], 
      "wind_deg": 286, 
      "wind_gust": 5.92, 
      "wind_speed": 3.49
    }, 
    {
      "clouds": 100, 
      "dew_point": 284.62, 
      "dt": 1624359600, 
      "feels_like": {
        "day": 287.97, 
        "eve": 286.26, 
        "morn": 287.3, 
        "night": 284.21
      }, 
      "humidity": 79, 
      "moon_phase": 0.41, 
      "moonrise": 1624383060, 
      "moonset": 1624324680, 
      "pop": 0.43, 
      "pressure": 1013, 
      "rain": 1.09, 
      "sunrise": 1624331186, 
      "sunset": 1624392299, 
      "temp": {
        "day": 288.33, 
        "eve": 286.73, 
        "max": 288.33, 
        "min": 284.27, 
        "morn": 287.61, 
        "night": 284.75
      }, 
      "uvi": 7, 
      "weather": [
        {
          "description": "light rain", 
          "icon": "10d", 
          "id": 500, 
          "main": "Rain"
        }
      ], 
      "wind_deg": 284, 
      "wind_gust": 7.59, 
      "wind_speed": 5.35
    }, 
    {
      "clouds": 44, 
      "dew_point": 280.91, 
      "dt": 1624446000, 
      "feels_like": {
        "day": 288.87, 
        "eve": 287.62, 
        "morn": 284.25, 
        "night": 282.62
      }, 
      "humidity": 56, 
      "moon_phase": 0.45, 
      "moonrise": 1624474860, 
      "moonset": 1624412760, 
      "pop": 0.54, 
      "pressure": 1022, 
      "rain": 1.44, 
      "sunrise": 1624417603, 
      "sunset": 1624478706, 
      "temp": {
        "day": 289.7, 
        "eve": 288.25, 
        "max": 289.82, 
        "min": 281.04, 
        "morn": 284.83, 
        "night": 283.26
      }, 
      "uvi": 7, 
      "weather": [
        {
          "description": "light rain", 
          "icon": "10d", 
          "id": 500, 
          "main": "Rain"
        }
      ], 
      "wind_deg": 304, 
      "wind_gust": 8.95, 
      "wind_speed": 6.66
    }, 
    {
      "clouds": 100, 
      "dew_point": 284.35, 
      "dt": 1624532400, 
      "feels_like": {
        "day": 287.33, 
        "eve": 287.82, 
        "morn": 285.76, 
        "night": 287
      }, 
      "humidity": 80, 
      "moon_phase": 0.5, 
      "moonrise": 1624566060, 
      "moonset": 1624501440, 
      "pop": 0.52, 
      "pressure": 1020, 
      "rain": 0.34, 
      "sunrise": 1624504023, 
      "sunset": 1624565110, 
      "temp": {
        "day": 287.73, 
        "eve": 288.05, 
        "max": 288.05, 
        "min": 281.11, 
        "morn": 286.28, 
        "night": 287.12
      }, 
      "uvi": 7, 
      "weather": [
        {
          "description": "light rain", 
          "icon": "10d", 
          "id": 500, 
          "main": "Rain"
        }
      ], 
      "wind_deg": 220, 
      "wind_gust": 11.73, 
      "wind_speed": 6.6
    }
  ], 
  "hourly": [
    {
      "clouds": 39, 
      "dew_point": 291.94, 
      "dt": 1623949200, 
      "feels_like": 301.24, 
      "humidity": 61, 
      "pop": 0.78, 
      "pressure": 1011, 
      "temp": 300.1, 
      "uvi": 1.04, 
      "visibility": 10000, 
      "weather": [
        {
          "description": "scattered clouds", 
          "icon": "03d", 
          "id": 802, 
          "main": "Clouds"
        }
      ], 
      "wind_deg": 289, 
      "wind_gust": 7.63, 
      "wind_speed": 5.35
    }, 
    {
      "clouds": 38, 
      "dew_point": 292.29, 
      "dt": 1623952800, 
      "feels_like": 299.13, 
      "humidity": 66, 
      "pop": 0.7, 
      "pressure": 1011, 
      "temp": 299.13, 
      "uvi": 0.42, 
      "visibility": 10000, 
      "weather": [
        {
          "description": "scattered clouds", 
          "icon": "03d", 
          "id": 802, 
          "main": "Clouds"
        }
      ], 
      "wind_deg": 282, 
      "wind_gust": 6.95, 
      "wind_speed": 3.46
    }, 
    {
      "clouds": 23, 
      "dew_point": 292.53, 
      "dt": 1623956400, 
      "feels_like": 297.88, 
      "humidity": 74, 
      "pop": 0.76, 
      "pressure": 1011, 
      "temp": 297.46, 
      "uvi": 0.11, 
      "visibility": 10000, 
      "weather": [
        {
          "description": "few clouds", 
          "icon": "02d", 
          "id": 801, 
          "main": "Clouds"
        }
      ], 
      "wind_deg": 307, 
      "wind_gust": 3.59, 
      "wind_speed": 1.89
    }, 
    {
      "clouds": 17, 
      "dew_point": 291.76, 
      "dt": 1623960000, 
      "feels_like": 295.35, 
      "humidity": 82, 
      "pop": 0.68, 
      "pressure": 1012, 
      "temp": 294.97, 
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
      "wind_deg": 332, 
      "wind_gust": 3.89, 
      "wind_speed": 2.77
    }, 
    {
      "clouds": 10, 
      "dew_point": 290.46, 
      "dt": 1623963600, 
      "feels_like": 292.62, 
      "humidity": 89, 
      "pop": 0.62, 
      "pressure": 1013, 
      "temp": 292.32, 
      "uvi": 0, 
      "visibility": 10000, 
      "weather": [
        {
          "description": "clear sky", 
          "icon": "01n", 
          "id": 800, 
          "main": "Clear"
        }
      ], 
      "wind_deg": 355, 
      "wind_gust": 4.28, 
      "wind_speed": 2.82
    }, 
    {
      "clouds": 12, 
      "dew_point": 289.29, 
      "dt": 1623967200, 
      "feels_like": 290.31, 
      "humidity": 95, 
      "pop": 0.66, 
      "pressure": 1014, 
      "temp": 290.08, 
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
      "wind_deg": 330, 
      "wind_gust": 2.46, 
      "wind_speed": 2.24
    }, 
    {
      "clouds": 29, 
      "dew_point": 289.11, 
      "dt": 1623970800, 
      "feels_like": 290.22, 
      "humidity": 95, 
      "pop": 0.55, 
      "pressure": 1014, 
      "temp": 290, 
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
      "wind_deg": 351, 
      "wind_gust": 1.68, 
      "wind_speed": 1.66
    }, 
    {
      "clouds": 41, 
      "dew_point": 289, 
      "dt": 1623974400, 
      "feels_like": 290.14, 
      "humidity": 94, 
      "pop": 0.43, 
      "pressure": 1013, 
      "temp": 289.95, 
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
      "wind_deg": 31, 
      "wind_gust": 1.92, 
      "wind_speed": 1.93
    }, 
    {
      "clouds": 100, 
      "dew_point": 288.77, 
      "dt": 1623978000, 
      "feels_like": 289.99, 
      "humidity": 93, 
      "pop": 0.01, 
      "pressure": 1013, 
      "temp": 289.84, 
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
      "wind_gust": 1.15, 
      "wind_speed": 1.13
    }, 
    {
      "clouds": 100, 
      "dew_point": 288.78, 
      "dt": 1623981600, 
      "feels_like": 290.08, 
      "humidity": 93, 
      "pop": 0.01, 
      "pressure": 1013, 
      "temp": 289.92, 
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
      "wind_deg": 37, 
      "wind_gust": 1.56, 
      "wind_speed": 1.54
    }, 
    {
      "clouds": 100, 
      "dew_point": 288.73, 
      "dt": 1623985200, 
      "feels_like": 289.93, 
      "humidity": 93, 
      "pop": 0.02, 
      "pressure": 1013, 
      "temp": 289.78, 
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
      "wind_deg": 18, 
      "wind_gust": 1.8, 
      "wind_speed": 1.76
    }, 
    {
      "clouds": 100, 
      "dew_point": 289.02, 
      "dt": 1623988800, 
      "feels_like": 290.14, 
      "humidity": 94, 
      "pop": 0.08, 
      "pressure": 1013, 
      "temp": 289.95, 
      "uvi": 0.05, 
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
      "wind_gust": 2.42, 
      "wind_speed": 2.22
    }, 
    {
      "clouds": 100, 
      "dew_point": 289.82, 
      "dt": 1623992400, 
      "feels_like": 291.36, 
      "humidity": 92, 
      "pop": 0.18, 
      "pressure": 1013, 
      "temp": 291.11, 
      "uvi": 0.17, 
      "visibility": 10000, 
      "weather": [
        {
          "description": "overcast clouds", 
          "icon": "04d", 
          "id": 804, 
          "main": "Clouds"
        }
      ], 
      "wind_deg": 48, 
      "wind_gust": 2.69, 
      "wind_speed": 1.82
    }, 
    {
      "clouds": 100, 
      "dew_point": 290.38, 
      "dt": 1623996000, 
      "feels_like": 292.65, 
      "humidity": 88, 
      "pop": 0.22, 
      "pressure": 1013, 
      "rain": {
        "1h": 0.33
      }, 
      "temp": 292.37, 
      "uvi": 0.42, 
      "visibility": 10000, 
      "weather": [
        {
          "description": "light rain", 
          "icon": "10d", 
          "id": 500, 
          "main": "Rain"
        }
      ], 
      "wind_deg": 84, 
      "wind_gust": 2.19, 
      "wind_speed": 1.48
    }, 
    {
      "clouds": 100, 
      "dew_point": 290.99, 
      "dt": 1623999600, 
      "feels_like": 293.81, 
      "humidity": 85, 
      "pop": 1, 
      "pressure": 1014, 
      "rain": {
        "1h": 0.83
      }, 
      "temp": 293.5, 
      "uvi": 1.2, 
      "visibility": 10000, 
      "weather": [
        {
          "description": "light rain", 
          "icon": "10d", 
          "id": 500, 
          "main": "Rain"
        }
      ], 
      "wind_deg": 87, 
      "wind_gust": 1.13, 
      "wind_speed": 0.92
    }, 
    {
      "clouds": 100, 
      "dew_point": 291.35, 
      "dt": 1624003200, 
      "feels_like": 294.12, 
      "humidity": 86, 
      "pop": 1, 
      "pressure": 1013, 
      "rain": {
        "1h": 0.55
      }, 
      "temp": 293.76, 
      "uvi": 2.01, 
      "visibility": 10000, 
      "weather": [
        {
          "description": "light rain", 
          "icon": "10d", 
          "id": 500, 
          "main": "Rain"
        }
      ], 
      "wind_deg": 60, 
      "wind_gust": 2.77, 
      "wind_speed": 2.27
    }, 
    {
      "clouds": 100, 
      "dew_point": 291.78, 
      "dt": 1624006800, 
      "feels_like": 295.47, 
      "humidity": 82, 
      "pop": 0.97, 
      "pressure": 1012, 
      "rain": {
        "1h": 0.11
      }, 
      "temp": 295.08, 
      "uvi": 2.91, 
      "visibility": 10000, 
      "weather": [
        {
          "description": "light rain", 
          "icon": "10d", 
          "id": 500, 
          "main": "Rain"
        }
      ], 
      "wind_deg": 51, 
      "wind_gust": 3.53, 
      "wind_speed": 3.21
    }, 
    {
      "clouds": 100, 
      "dew_point": 291.99, 
      "dt": 1624010400, 
      "feels_like": 295.85, 
      "humidity": 80, 
      "pop": 0.77, 
      "pressure": 1012, 
      "temp": 295.47, 
      "uvi": 4.25, 
      "visibility": 10000, 
      "weather": [
        {
          "description": "overcast clouds", 
          "icon": "04d", 
          "id": 804, 
          "main": "Clouds"
        }
      ], 
      "wind_deg": 50, 
      "wind_gust": 3.99, 
      "wind_speed": 3.86
    }, 
    {
      "clouds": 100, 
      "dew_point": 292.22, 
      "dt": 1624014000, 
      "feels_like": 296.8, 
      "humidity": 77, 
      "pop": 0.9, 
      "pressure": 1013, 
      "temp": 296.41, 
      "uvi": 4.78, 
      "visibility": 10000, 
      "weather": [
        {
          "description": "overcast clouds", 
          "icon": "04d", 
          "id": 804, 
          "main": "Clouds"
        }
      ], 
      "wind_deg": 59, 
      "wind_gust": 3.49, 
      "wind_speed": 3.03
    }, 
    {
      "clouds": 100, 
      "dew_point": 292.91, 
      "dt": 1624017600, 
      "feels_like": 298.2, 
      "humidity": 75, 
      "pop": 0.87, 
      "pressure": 1012, 
      "temp": 297.73, 
      "uvi": 4.82, 
      "visibility": 10000, 
      "weather": [
        {
          "description": "overcast clouds", 
          "icon": "04d", 
          "id": 804, 
          "main": "Clouds"
        }
      ], 
      "wind_deg": 54, 
      "wind_gust": 3.69, 
      "wind_speed": 2.86
    }, 
    {
      "clouds": 94, 
      "dew_point": 293.33, 
      "dt": 1624021200, 
      "feels_like": 299.16, 
      "humidity": 72, 
      "pop": 0.53, 
      "pressure": 1011, 
      "rain": {
        "1h": 0.14
      }, 
      "temp": 298.67, 
      "uvi": 4.59, 
      "visibility": 10000, 
      "weather": [
        {
          "description": "light rain", 
          "icon": "10d", 
          "id": 500, 
          "main": "Rain"
        }
      ], 
      "wind_deg": 61, 
      "wind_gust": 4.52, 
      "wind_speed": 3.22
    }, 
    {
      "clouds": 82, 
      "dew_point": 293.72, 
      "dt": 1624024800, 
      "feels_like": 299.6, 
      "humidity": 70, 
      "pop": 0.64, 
      "pressure": 1011, 
      "rain": {
        "1h": 0.79
      }, 
      "temp": 299.6, 
      "uvi": 3.69, 
      "visibility": 10000, 
      "weather": [
        {
          "description": "light rain", 
          "icon": "10d", 
          "id": 500, 
          "main": "Rain"
        }
      ], 
      "wind_deg": 96, 
      "wind_gust": 4.53, 
      "wind_speed": 2.34
    }, 
    {
      "clouds": 61, 
      "dew_point": 293.71, 
      "dt": 1624028400, 
      "feels_like": 301.67, 
      "humidity": 68, 
      "pop": 0.91, 
      "pressure": 1011, 
      "rain": {
        "1h": 0.84
      }, 
      "temp": 300.04, 
      "uvi": 2.61, 
      "visibility": 8017, 
      "weather": [
        {
          "description": "light rain", 
          "icon": "10d", 
          "id": 500, 
          "main": "Rain"
        }
      ], 
      "wind_deg": 131, 
      "wind_gust": 5.69, 
      "wind_speed": 2.4
    }, 
    {
      "clouds": 49, 
      "dew_point": 293.78, 
      "dt": 1624032000, 
      "feels_like": 302.29, 
      "humidity": 67, 
      "pop": 0.88, 
      "pressure": 1010, 
      "rain": {
        "1h": 0.67
      }, 
      "temp": 300.48, 
      "uvi": 2.06, 
      "visibility": 10000, 
      "weather": [
        {
          "description": "light rain", 
          "icon": "10d", 
          "id": 500, 
          "main": "Rain"
        }
      ], 
      "wind_deg": 144, 
      "wind_gust": 5.87, 
      "wind_speed": 2.05
    }, 
    {
      "clouds": 40, 
      "dew_point": 294.42, 
      "dt": 1624035600, 
      "feels_like": 302.58, 
      "humidity": 69, 
      "pop": 0.84, 
      "pressure": 1009, 
      "rain": {
        "1h": 0.22
      }, 
      "temp": 300.54, 
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
      "wind_deg": 165, 
      "wind_gust": 6.53, 
      "wind_speed": 1.98
    }, 
    {
      "clouds": 50, 
      "dew_point": 293.8, 
      "dt": 1624039200, 
      "feels_like": 298.52, 
      "humidity": 78, 
      "pop": 0.84, 
      "pressure": 1009, 
      "temp": 297.95, 
      "uvi": 0.42, 
      "visibility": 10000, 
      "weather": [
        {
          "description": "scattered clouds", 
          "icon": "03d", 
          "id": 802, 
          "main": "Clouds"
        }
      ], 
      "wind_deg": 119, 
      "wind_gust": 1.99, 
      "wind_speed": 1.28
    }, 
    {
      "clouds": 100, 
      "dew_point": 293.46, 
      "dt": 1624042800, 
      "feels_like": 297.73, 
      "humidity": 80, 
      "pop": 0.61, 
      "pressure": 1009, 
      "rain": {
        "1h": 0.12
      }, 
      "temp": 297.18, 
      "uvi": 0.03, 
      "visibility": 10000, 
      "weather": [
        {
          "description": "light rain", 
          "icon": "10d", 
          "id": 500, 
          "main": "Rain"
        }
      ], 
      "wind_deg": 164, 
      "wind_gust": 2.98, 
      "wind_speed": 1.84
    }, 
    {
      "clouds": 65, 
      "dew_point": 292.48, 
      "dt": 1624046400, 
      "feels_like": 295.53, 
      "humidity": 86, 
      "pop": 0.67, 
      "pressure": 1010, 
      "rain": {
        "1h": 0.6
      }, 
      "temp": 295.04, 
      "uvi": 0, 
      "visibility": 10000, 
      "weather": [
        {
          "description": "light rain", 
          "icon": "10d", 
          "id": 500, 
          "main": "Rain"
        }
      ], 
      "wind_deg": 215, 
      "wind_gust": 8.03, 
      "wind_speed": 3.44
    }, 
    {
      "clouds": 64, 
      "dew_point": 291.71, 
      "dt": 1624050000, 
      "feels_like": 295.02, 
      "humidity": 83, 
      "pop": 0.72, 
      "pressure": 1010, 
      "rain": {
        "1h": 0.15
      }, 
      "temp": 294.65, 
      "uvi": 0, 
      "visibility": 10000, 
      "weather": [
        {
          "description": "light rain", 
          "icon": "10n", 
          "id": 500, 
          "main": "Rain"
        }
      ], 
      "wind_deg": 219, 
      "wind_gust": 11.9, 
      "wind_speed": 4.71
    }, 
    {
      "clouds": 70, 
      "dew_point": 291.13, 
      "dt": 1624053600, 
      "feels_like": 294, 
      "humidity": 85, 
      "pop": 0.69, 
      "pressure": 1010, 
      "temp": 293.67, 
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
      "wind_deg": 206, 
      "wind_gust": 12.17, 
      "wind_speed": 4.76
    }, 
    {
      "clouds": 76, 
      "dew_point": 290.61, 
      "dt": 1624057200, 
      "feels_like": 293.6, 
      "humidity": 84, 
      "pop": 0.69, 
      "pressure": 1011, 
      "temp": 293.33, 
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
      "wind_deg": 186, 
      "wind_gust": 11.84, 
      "wind_speed": 5.6
    }, 
    {
      "clouds": 80, 
      "dew_point": 290.32, 
      "dt": 1624060800, 
      "feels_like": 292.75, 
      "humidity": 87, 
      "pop": 0.68, 
      "pressure": 1010, 
      "temp": 292.49, 
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
      "wind_deg": 201, 
      "wind_gust": 10.9, 
      "wind_speed": 5.21
    }, 
    {
      "clouds": 0, 
      "dew_point": 289.21, 
      "dt": 1624064400, 
      "feels_like": 291.3, 
      "humidity": 88, 
      "pop": 0, 
      "pressure": 1010, 
      "temp": 291.15, 
      "uvi": 0, 
      "visibility": 10000, 
      "weather": [
        {
          "description": "clear sky", 
          "icon": "01n", 
          "id": 800, 
          "main": "Clear"
        }
      ], 
      "wind_deg": 207, 
      "wind_gust": 13.65, 
      "wind_speed": 6.06
    }, 
    {
      "clouds": 1, 
      "dew_point": 287.72, 
      "dt": 1624068000, 
      "feels_like": 289.4, 
      "humidity": 90, 
      "pop": 0, 
      "pressure": 1010, 
      "temp": 289.37, 
      "uvi": 0, 
      "visibility": 10000, 
      "weather": [
        {
          "description": "clear sky", 
          "icon": "01n", 
          "id": 800, 
          "main": "Clear"
        }
      ], 
      "wind_deg": 205, 
      "wind_gust": 15.19, 
      "wind_speed": 7.68
    }, 
    {
      "clouds": 5, 
      "dew_point": 286.45, 
      "dt": 1624071600, 
      "feels_like": 287.9, 
      "humidity": 90, 
      "pop": 0, 
      "pressure": 1010, 
      "temp": 288.01, 
      "uvi": 0, 
      "visibility": 10000, 
      "weather": [
        {
          "description": "clear sky", 
          "icon": "01n", 
          "id": 800, 
          "main": "Clear"
        }
      ], 
      "wind_deg": 202, 
      "wind_gust": 16.43, 
      "wind_speed": 8.36
    }, 
    {
      "clouds": 13, 
      "dew_point": 285.27, 
      "dt": 1624075200, 
      "feels_like": 287.28, 
      "humidity": 86, 
      "pop": 0, 
      "pressure": 1010, 
      "temp": 287.54, 
      "uvi": 0.03, 
      "visibility": 10000, 
      "weather": [
        {
          "description": "few clouds", 
          "icon": "02d", 
          "id": 801, 
          "main": "Clouds"
        }
      ], 
      "wind_deg": 205, 
      "wind_gust": 17.03, 
      "wind_speed": 9.34
    }, 
    {
      "clouds": 30, 
      "dew_point": 285.6, 
      "dt": 1624078800, 
      "feels_like": 287.68, 
      "humidity": 86, 
      "pop": 0, 
      "pressure": 1011, 
      "temp": 287.9, 
      "uvi": 0.11, 
      "visibility": 10000, 
      "weather": [
        {
          "description": "scattered clouds", 
          "icon": "03d", 
          "id": 802, 
          "main": "Clouds"
        }
      ], 
      "wind_deg": 210, 
      "wind_gust": 16.95, 
      "wind_speed": 9.72
    }, 
    {
      "clouds": 41, 
      "dew_point": 286.65, 
      "dt": 1624082400, 
      "feels_like": 288.71, 
      "humidity": 87, 
      "pop": 0, 
      "pressure": 1011, 
      "temp": 288.82, 
      "uvi": 0.28, 
      "visibility": 10000, 
      "weather": [
        {
          "description": "scattered clouds", 
          "icon": "03d", 
          "id": 802, 
          "main": "Clouds"
        }
      ], 
      "wind_deg": 228, 
      "wind_gust": 16.08, 
      "wind_speed": 9.55
    }, 
    {
      "clouds": 97, 
      "dew_point": 287.16, 
      "dt": 1624086000, 
      "feels_like": 289.87, 
      "humidity": 83, 
      "pop": 0, 
      "pressure": 1012, 
      "temp": 289.97, 
      "uvi": 0.38, 
      "visibility": 10000, 
      "weather": [
        {
          "description": "overcast clouds", 
          "icon": "04d", 
          "id": 804, 
          "main": "Clouds"
        }
      ], 
      "wind_deg": 255, 
      "wind_gust": 15.19, 
      "wind_speed": 9.21
    }, 
    {
      "clouds": 89, 
      "dew_point": 286.09, 
      "dt": 1624089600, 
      "feels_like": 289.25, 
      "humidity": 80, 
      "pop": 0, 
      "pressure": 1014, 
      "temp": 289.47, 
      "uvi": 0.64, 
      "visibility": 10000, 
      "weather": [
        {
          "description": "overcast clouds", 
          "icon": "04d", 
          "id": 804, 
          "main": "Clouds"
        }
      ], 
      "wind_deg": 287, 
      "wind_gust": 13.74, 
      "wind_speed": 9.28
    }, 
    {
      "clouds": 73, 
      "dew_point": 284.86, 
      "dt": 1624093200, 
      "feels_like": 288.91, 
      "humidity": 75, 
      "pop": 0, 
      "pressure": 1016, 
      "temp": 289.28, 
      "uvi": 0.92, 
      "visibility": 10000, 
      "weather": [
        {
          "description": "broken clouds", 
          "icon": "04d", 
          "id": 803, 
          "main": "Clouds"
        }
      ], 
      "wind_deg": 305, 
      "wind_gust": 10.95, 
      "wind_speed": 8.06
    }, 
    {
      "clouds": 59, 
      "dew_point": 284.69, 
      "dt": 1624096800, 
      "feels_like": 289.85, 
      "humidity": 69, 
      "pop": 0, 
      "pressure": 1016, 
      "temp": 290.28, 
      "uvi": 2.6, 
      "visibility": 10000, 
      "weather": [
        {
          "description": "broken clouds", 
          "icon": "04d", 
          "id": 803, 
          "main": "Clouds"
        }
      ], 
      "wind_deg": 303, 
      "wind_gust": 7.61, 
      "wind_speed": 6.04
    }, 
    {
      "clouds": 65, 
      "dew_point": 284.61, 
      "dt": 1624100400, 
      "feels_like": 290.21, 
      "humidity": 68, 
      "pop": 0, 
      "pressure": 1017, 
      "temp": 290.63, 
      "uvi": 2.92, 
      "visibility": 10000, 
      "weather": [
        {
          "description": "broken clouds", 
          "icon": "04d", 
          "id": 803, 
          "main": "Clouds"
        }
      ], 
      "wind_deg": 306, 
      "wind_gust": 5.92, 
      "wind_speed": 5.28
    }, 
    {
      "clouds": 70, 
      "dew_point": 284.72, 
      "dt": 1624104000, 
      "feels_like": 290.41, 
      "humidity": 67, 
      "pop": 0, 
      "pressure": 1017, 
      "temp": 290.84, 
      "uvi": 2.95, 
      "visibility": 10000, 
      "weather": [
        {
          "description": "broken clouds", 
          "icon": "04d", 
          "id": 803, 
          "main": "Clouds"
        }
      ], 
      "wind_deg": 310, 
      "wind_gust": 5.05, 
      "wind_speed": 4.78
    }, 
    {
      "clouds": 52, 
      "dew_point": 284.88, 
      "dt": 1624107600, 
      "feels_like": 290.62, 
      "humidity": 67, 
      "pop": 0, 
      "pressure": 1017, 
      "temp": 291.03, 
      "uvi": 3.68, 
      "visibility": 10000, 
      "weather": [
        {
          "description": "broken clouds", 
          "icon": "04d", 
          "id": 803, 
          "main": "Clouds"
        }
      ], 
      "wind_deg": 318, 
      "wind_gust": 3.79, 
      "wind_speed": 4.02
    }, 
    {
      "clouds": 67, 
      "dew_point": 284.88, 
      "dt": 1624111200, 
      "feels_like": 290.2, 
      "humidity": 69, 
      "pop": 0, 
      "pressure": 1017, 
      "temp": 290.6, 
      "uvi": 2.95, 
      "visibility": 10000, 
      "weather": [
        {
          "description": "broken clouds", 
          "icon": "04d", 
          "id": 803, 
          "main": "Clouds"
        }
      ], 
      "wind_deg": 333, 
      "wind_gust": 3.12, 
      "wind_speed": 4.01
    }, 
    {
      "clouds": 77, 
      "dew_point": 284.59, 
      "dt": 1624114800, 
      "feels_like": 289.57, 
      "humidity": 70, 
      "pop": 0, 
      "pressure": 1018, 
      "temp": 290, 
      "uvi": 2.09, 
      "visibility": 10000, 
      "weather": [
        {
          "description": "broken clouds", 
          "icon": "04d", 
          "id": 803, 
          "main": "Clouds"
        }
      ], 
      "wind_deg": 342, 
      "wind_gust": 2.58, 
      "wind_speed": 3.75
    }, 
    {
      "clouds": 83, 
      "dew_point": 284.32, 
      "dt": 1624118400, 
      "feels_like": 288.85, 
      "humidity": 73, 
      "pop": 0, 
      "pressure": 1017, 
      "temp": 289.28, 
      "uvi": 1.63, 
      "visibility": 10000, 
      "weather": [
        {
          "description": "broken clouds", 
          "icon": "04d", 
          "id": 803, 
          "main": "Clouds"
        }
      ], 
      "wind_deg": 4, 
      "wind_gust": 3.83, 
      "wind_speed": 4.45
    }
  ], 
  "lat": 53.2192, 
  "lon": 6.5667, 
  "minutely": [
    {
      "dt": 1623949500, 
      "precipitation": 0
    }, 
    {
      "dt": 1623949560, 
      "precipitation": 0
    }, 
    {
      "dt": 1623949620, 
      "precipitation": 0
    }, 
    {
      "dt": 1623949680, 
      "precipitation": 0
    }, 
    {
      "dt": 1623949740, 
      "precipitation": 0
    }, 
    {
      "dt": 1623949800, 
      "precipitation": 0
    }, 
    {
      "dt": 1623949860, 
      "precipitation": 0
    }, 
    {
      "dt": 1623949920, 
      "precipitation": 0
    }, 
    {
      "dt": 1623949980, 
      "precipitation": 0
    }, 
    {
      "dt": 1623950040, 
      "precipitation": 0
    }, 
    {
      "dt": 1623950100, 
      "precipitation": 0
    }, 
    {
      "dt": 1623950160, 
      "precipitation": 0
    }, 
    {
      "dt": 1623950220, 
      "precipitation": 0
    }, 
    {
      "dt": 1623950280, 
      "precipitation": 0
    }, 
    {
      "dt": 1623950340, 
      "precipitation": 0
    }, 
    {
      "dt": 1623950400, 
      "precipitation": 0
    }, 
    {
      "dt": 1623950460, 
      "precipitation": 0
    }, 
    {
      "dt": 1623950520, 
      "precipitation": 0
    }, 
    {
      "dt": 1623950580, 
      "precipitation": 0
    }, 
    {
      "dt": 1623950640, 
      "precipitation": 0
    }, 
    {
      "dt": 1623950700, 
      "precipitation": 0
    }, 
    {
      "dt": 1623950760, 
      "precipitation": 0
    }, 
    {
      "dt": 1623950820, 
      "precipitation": 0
    }, 
    {
      "dt": 1623950880, 
      "precipitation": 0
    }, 
    {
      "dt": 1623950940, 
      "precipitation": 0
    }, 
    {
      "dt": 1623951000, 
      "precipitation": 0
    }, 
    {
      "dt": 1623951060, 
      "precipitation": 0
    }, 
    {
      "dt": 1623951120, 
      "precipitation": 0
    }, 
    {
      "dt": 1623951180, 
      "precipitation": 0
    }, 
    {
      "dt": 1623951240, 
      "precipitation": 0
    }, 
    {
      "dt": 1623951300, 
      "precipitation": 0
    }, 
    {
      "dt": 1623951360, 
      "precipitation": 0
    }, 
    {
      "dt": 1623951420, 
      "precipitation": 0
    }, 
    {
      "dt": 1623951480, 
      "precipitation": 0
    }, 
    {
      "dt": 1623951540, 
      "precipitation": 0
    }, 
    {
      "dt": 1623951600, 
      "precipitation": 0
    }, 
    {
      "dt": 1623951660, 
      "precipitation": 0
    }, 
    {
      "dt": 1623951720, 
      "precipitation": 0
    }, 
    {
      "dt": 1623951780, 
      "precipitation": 0
    }, 
    {
      "dt": 1623951840, 
      "precipitation": 0
    }, 
    {
      "dt": 1623951900, 
      "precipitation": 0
    }, 
    {
      "dt": 1623951960, 
      "precipitation": 0
    }, 
    {
      "dt": 1623952020, 
      "precipitation": 0
    }, 
    {
      "dt": 1623952080, 
      "precipitation": 0
    }, 
    {
      "dt": 1623952140, 
      "precipitation": 0
    }, 
    {
      "dt": 1623952200, 
      "precipitation": 0
    }, 
    {
      "dt": 1623952260, 
      "precipitation": 0
    }, 
    {
      "dt": 1623952320, 
      "precipitation": 0
    }, 
    {
      "dt": 1623952380, 
      "precipitation": 0
    }, 
    {
      "dt": 1623952440, 
      "precipitation": 0
    }, 
    {
      "dt": 1623952500, 
      "precipitation": 0
    }, 
    {
      "dt": 1623952560, 
      "precipitation": 0
    }, 
    {
      "dt": 1623952620, 
      "precipitation": 0
    }, 
    {
      "dt": 1623952680, 
      "precipitation": 0
    }, 
    {
      "dt": 1623952740, 
      "precipitation": 0
    }, 
    {
      "dt": 1623952800, 
      "precipitation": 0
    }, 
    {
      "dt": 1623952860, 
      "precipitation": 0
    }, 
    {
      "dt": 1623952920, 
      "precipitation": 0
    }, 
    {
      "dt": 1623952980, 
      "precipitation": 0
    }, 
    {
      "dt": 1623953040, 
      "precipitation": 0
    }, 
    {
      "dt": 1623953100, 
      "precipitation": 0
    }
  ], 
  "timezone": "Europe/Amsterdam", 
  "timezone_offset": 7200
}
"""
