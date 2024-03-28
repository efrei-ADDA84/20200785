class DonneesMeteo:
    def __init__(self, data):
        self.coordonnees = data['coord']
        self.meteo = data['weather'][0]
        self.base = data['base']
        self.temperature = data['main']['temp']
        self.sensation = data['main']['feels_like']
        self.temperature_min = data['main']['temp_min']
        self.temperature_max = data['main']['temp_max']
        self.pression = data['main']['pressure']
        self.humidite = data['main']['humidity']
        self.visibilite = data['visibility']
        self.vent = data['wind']
        self.nuages = data['clouds']
        self.lever_soleil = data['sys']['sunrise']
        self.coucher_soleil = data['sys']['sunset']
        self.timezone = data['timezone']
        self.nom = data['name']
        self.pays = data['sys']['country']

    def __str__(self):
        return f"Météo à {self.nom}, {self.pays}:\n" \
               f"Température: {self.temperature}°C\n" \
               f"Sensation: {self.sensation}°C\n" \
               f"Température minimale: {self.temperature_min}°C\n" \
               f"Température maximale: {self.temperature_max}°C\n" \
               f"Pression: {self.pression} hPa\n" \
               f"Humidité: {self.humidite}%\n" \
               f"Visibilité: {self.visibilite} mètres\n" \
               f"Vitesse du vent: {self.vent['speed']} m/s\n" \
               f"Nuages: {self.nuages['all']}%\n" \
               f"Lever du soleil: {self.lever_soleil}\n" \
               f"Coucher du soleil: {self.coucher_soleil}\n" \
               f"Fuseau horaire: {self.timezone}"
