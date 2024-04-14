# Etapes :
## Création du main :
os.getenv permet de récupérer les variables d'environnement et requests.get(url) permet de récupérer les données à l'url renseigné.
On accède ensuite au wrapper

## le fichier wrapper.py :
Ici, on crée une classe qui va permettre de bien afficher les données, après une analyse du résultat obtenu.  On peut ainsi visualiser toutes
les informations liées à la météo.

## Dockerfile :
On crée ensuite le dockerfile, en spécifiant la version de python, le pip install de requests et la commande à faire pour lancer.

## Création de l'image docker :
```docker build -t image_meteo . ``` : permet de créer l'image
```docker run --env LAT="48.866667" --env LONG="2.333333" --env APIKEY='f56a6cc9d2d2762c923e663630dc6615' image_meteo ```=> executer le conteneur docker avec les variables d'environnement

## Mettre à disposition son image sur dockerhub :

```docker login``` : pour se connecter
```docker tag image_meteo felixdvk/image_meteo:1.0``` => étiquette l'image locale image_meteo avec le nom felixdvk/image_meteo:1.0
```docker push felixdvk/image_meteo:1.0``` => pousser l'image vers Docker Hub.

## Configuration d'un workflow sur Github :
Ce workflow permet d'automatiser les taches. Il fonctionne à travers des name (nom de la tache) et run (commande que github doit exécuter).   Il est possible d'utiliser des github actions mais j'ai choisi de n'écrire que les tâches à la main.  Par ailleurs, j'ai cherché à utiliser des docker actions, par exemple "docker/login-action@v2" pour se connecter et c'est assez similaire. 
Dans ce workflow, nous nous connectons à dockerHub (avec des variables secrètes configurées dans github), on build l'image et on la push.

## Transformer le wrapper en API :
Pour cela, j'ai utilisé la librairie flask, puis pour lancer l'application, j'ai fait : ```python app.py``` ;  Je peux visualiser le résultat sur l'adresse suivant :  http://127.0.0.1:8081 . Voici un exemple obtenu : '{"Meteo":"broken clouds","temperature":15.08}'. En cas de problème de récupération de la latitude et longitude avec 'request.args.get', écrire les valeurs de manières concrètes 'lat = 48.866667' peut permettre de visualiser les résultats. Enfin, la commande ```curl "http://localhost:8081/?lat=48.866667&lon=2.333333"``` permet de récupérer le contenu de l'url et de l'afficher dans le terminal.  ```@app.route``` est un décorateur qui définit la route dans notre application. Pour le reste, cela ressemble au main. J'ai essayé d'utiliser prometheus pour créer un compteur de requête qui est un exemple parmi tant d'autres.

