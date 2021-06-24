from app.utils import init_routing_func
from app.weather import Weather

device, get, post, put, delete = init_routing_func('device', '/api/device/')


@get('/weather')
def get_weather():
    #get these from the db
    lat = 53.21917
    lon = 5.6667
    return Weather.get_weather_by_coords(lat, lon)
