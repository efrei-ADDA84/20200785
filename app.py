from flask import Flask, jsonify, request
import requests
import os
from prometheus_client import Counter

appli = Flask(__name__)

# compter le nombre de requetes 
request_cpt = Counter('nb_requetes', 'Nombre requetes total')

@appli.route('/', methods=['GET'])
def obtenir_meteo():

    request_cpt.inc() # on incremente le compteur à chaque nouvelle requete

    lat = request.args.get("lat")
    long = request.args.get("lon")

    if lat is None or long is None:
        return jsonify({'error': 'Latitude et longitude ?????'}), 400

    api_key = os.environ.get("APIKEY")
    if not api_key:
        return jsonify({'error': 'Clé API OpenWeather ????'}), 500

    url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={long}&appid={api_key}&units=metric"
    reponse = requests.get(url)
    donnees = reponse.json()

    if reponse.status_code == 200:
        description = donnees['weather'][0]['description'] #  Récupérer les informations sur le ciel
        temperature = donnees['main']['temp'] # et sur la température
        return jsonify({'Meteo': description, 'temperature': temperature}), 200
    else:
        return jsonify({'error': 'Problème de récupération des données...'}), 500


if __name__ == '__main__':
    appli.run(host='0.0.0.0', port=8081)
