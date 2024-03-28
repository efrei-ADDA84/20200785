import os
import requests
from wrapper import DonneesMeteo

def get_weather(latitude, longitude):
    api_key = os.getenv("APIKEY")
    if not api_key:
        raise ValueError("Veuillez configurer la variable 'OPENWEATHER_API_KEY' !!!")

    url = f"http://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()

    return data

if __name__ == "__main__":
    latitude = os.getenv("LAT")
    longitude = os.getenv("LONG")

    if latitude is None or longitude is None:
        raise ValueError("Veuillez configurer la latitude et la longitude !!!")

    donnees = get_weather(latitude, longitude)
    info_meteo=DonneesMeteo(donnees)
    print(info_meteo)
