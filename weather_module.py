import requests
import json
import datetime
from dadata import Dadata
from const import TOKEN, SECRET


def get_address_coordinate(address):
    dadata = Dadata(TOKEN, SECRET)
    result = dadata.clean("address", address)
    return result['geo_lat'], result['geo_lon']


def get_current_weather(address):
    latitude, longitude = get_address_coordinate(address)
    response = requests.get(
        "https://api.open-meteo.com/v1/forecast",
        params={
            "latitude": latitude,
            "longitude": longitude,
            "hourly": "temperature_2m"
        }
    )
    weather_data = response.json()
    times = weather_data["hourly"]["time"]
    temperatures = weather_data["hourly"]["temperature_2m"]
    current_time = datetime.datetime.now()

    for time, temperature in zip(times, temperatures):
        if datetime.datetime.fromisoformat(time) >= current_time:
            return float(temperature)
    return None
