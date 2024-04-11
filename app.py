from flask import Flask, jsonify
import requests
from wrapper import DonneesMeteo
import os

app = Flask(__name__)

@app.route('/meteo', methods=['GET'])
def obtenir_meteo():
    latitude = os.getenv("LAT")
    longitude = os.getenv("LONG")
    print(latitude)
    print(longitude)

    if latitude is None or longitude is None:
        return jsonify({'error': 'Latitude et longitude ?????'}), 400

    api_key = os.getenv("APIKEY")
    if not api_key:
        return jsonify({'error': 'Clé API OpenWeather ????'}), 500

    url = f"http://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={api_key}&units=metric"
    reponse = requests.get(url)
    donnees = reponse.json()

    info_meteo = DonneesMeteo(donnees)

    return jsonify(info_meteo.__dict__)

if __name__ == '__main__':
    app.run(debug=True)
