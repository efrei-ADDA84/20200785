# Etapes :
## 1 - Création du main :
os.getenv permet de récupérer les variables d'environnement et requests.get(url) permet de récupérer les données à l'url renseigné.
On accède ensuite au wrapper

## le fichier wrapper.py :
Ici, on crée une classe qui va permettre de bien afficher les données, après une analyse du résultat obtenu. On peut ainsi visualiser toutes
les informations liées à la météo.

## Dockerfile :
On crée ensuite le dockerfile, en spécifiant la version de python, le pip install de requests et la commande à faire pour lancer.

## Création de l'image docker :

docker build -t image_meteo . : permet de créer l'image
docker run --env LAT="48.866667" --env LONG="2.333333" --env APIKEY='f56a6cc9d2d2762c923e663630dc6615' image_meteo => executer le conteneur docker avec les variables d'environnement

## Mettre à disposition son image sur dockerhub :

docker login : pour se connecter
docker tag image_meteo felixdvk/image_meteo:1.0 => étiquette l'image locale image_meteo avec le nom felixdvk/image_meteo:1.0
docker push felixdvk/image_meteo:1.0 => pousser l'image vers Docker Hub.