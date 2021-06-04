# GearWheel-Bestway
<h2>Who, When 'n' Why ?</h2>

<p>J'ai develloppé cette plateforme seul dans le cadre de ma formation OpenClassrooms du parcours 'developpeur d'applications Python' durant les mois d'Avril/Mai 2021. Je suis ouvert à toute amélioration de votre part bien entendu si vous le désirez.</p>

<h2>Kesako ?</h2>

<p>GearWheel est un gestionnaire libre d'accès informatique déployé sur internet déstiné à organiser une entreprise dans le secteur du batiment. Dans l'idée il propose plusieurs applications telle que Bestway ayant chacune sa particularitée comme par exemple l'organisation des clients, des chantiers, du S.A.V, des contrats d'entretiens, des devis, de la facturation ou encore du stock. A l'heure actuelle seule Bestway est en service.<br>Bestway est donc une application parmis de futures autres dans GearWheel. Sa mission est de gerer intelligemment les trajets d'un dépanneur (du S.A.V.) au cours de sa journée en lui proposant le trajet le moins couteux en kilomêtre à vol d'oiseau pour cette première version. Par la suite seront pris en compte le réseau routier et dans l'idéal le traffic en temps réel. L'utilisateur se crée donc un compte et peux ensuite entrer toutes les adresses: le départ, l'arrivée et ensuite les arrêts pour ses dépannages à effectuer.</p>

<h2>Installation</h2>

1. Pour l'installer, créez un dossier en local et clonez le projet 'GearWheel' sur Github à l'adresse suivante :<br>
<em>https://github.com/thomsart/GearWheel</em>

2. Une fois fait créez votre environnement virtuel et activez le :<br>
<em>python -m venv env</em> (pour le créer)<br>
<em>.\env\Scripts\activate</em> (pour l'activer)

3. Une fois activé installé y toutes les dépendances néccéssaires au projet en tapant la commande suivante :<br>
<em>pip install -r requirements.txt</em>

4. Créez votre base de données à l'aide de Postgrès. Pensez à bien modifier les paramètres liés à votre base de données dans les 'settings.py' à l'url (dans votre projet) :<br>
'GearWheel/gearwheel/settings.py'

5. Ensuite éxécutez la commande suivante (à la racine soit /GearWheel)pour lancer le server en local sur votre machine afin de pouvoir l'ouvrir ensuite avec votre navigateur :<br>
<em>python manage.py runserver</em>

6. Enfin ouvrez votre navigateur web et tapez y la l'url suivante :<br>
<em>http://localhost:8000/bestway/</em> (ici '8000' sur ma machine mais regardez le numéro du votre dans le terminal lors de l'activation de votre server.)

7. Il vous est possible de lancer les tests et le coverage (couverture des test) après amélioration de votre part en éxécutant les commandes suivantes:<br>
<em>pytest</em> (lance tout les tests des applications)<br>
Et pour avoir la couverture des tests faites:<br>
<em>pytest --cov=address</em> (pour l'application 'address')<br>
<em>pytest --cov=bestway</em> (pour l'application 'bestway')<br>

<h2>Liens de la plateforme sur le web</h2>

<p>Vous pouvez toute-fois vous rendre sur le site en ligne à cette adresse:<br>
<em>http://138.68.130.22/bestway/</em></p>