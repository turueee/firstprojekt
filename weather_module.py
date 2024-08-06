import requests
import json
import datetime


def get_current_weather(latitude, longitude):
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
