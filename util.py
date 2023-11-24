import requests
from config import ThirdConfig


def get_weather_data(location):
    api_key = ThirdConfig.WEATHER_KEY
    base_url = ThirdConfig.WEATHER_URL
    location = location

    response = requests.get(f'{base_url}/forecast.json?key={api_key}&q={location}&days=1&aqi=no&alerts=no')
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None


def get_weather_forcast(location):
    api_key = ThirdConfig.WEATHER_KEY
    base_url = ThirdConfig.WEATHER_URL
    location = location

    response = requests.get(f'{base_url}/forecast.json?key={api_key}&q={location}&days=3&aqi=no&alerts=no')
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None


def get_flight_data(flight_number):
    headers = {'x-apikey': ThirdConfig.FLIGHT_KEY}
    url = ThirdConfig.FLIGHT_URL + flight_number
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        return data['flights'][0]
    else:
        return None
