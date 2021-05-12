#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
from operator import itemgetter, attrgetter


"""
Le but de l'algorithme est de trouver le chemin le moins couteux en terme de
distance en prenant en considération tout les arrêts demandés.

l'idée est la suivante:
On doit en realité réussir à faire le polygone qui possède le moins de côtés
avec tout les sommets demandés, ce qui en fait revient à vouloir avoir la forme
géométrique qui possède le plus petit périmètre pour le nombre de sommets
demandé. Pour ce faire il faut procéder comme suit:

1 - Ressencer dans une liste tout les cerlcles du plus grand au plus petit
possèdant le même centre (notre point de départ).

2 - On réalise ensuite un triangle que l'on matérialisera par une liste des
trois premiers points de la liste initale dont les trois sommets sont confondus
avec les trois premiers cercles de notre liste de départ. On désignera cette
liste comme la liste de fin. On retire donc les trois premiers points de la
liste de départ.

3 - On prend ensuite le premier point de la liste de départ (qui était le 4ème)
et on réalise le cercle le plus petit ayant pour centre ce point avec le point
de la liste obtenue grace à notre triangle. On regarde ensuit le cercle qui est
juste après en terme de grandeur. Une fois les cercles obtenue on place
ce quatrième point extrait de la liste de départ pour le placer dans la liste
de fin entre les deux points qui ont servis à tracer les deux cercles précédants.

4 - On prend ensuite le premier point de la liste de départ (qui était le 5ème)
pour repeter la même opération jusqu'à épuisement des points de la liste de
départ. On obtient donc, grâce à notre liste de fin si on traçait les
droites qui relient dans l'ordre des points, ce polygone qui possède pour sommets
tout ces points de la liste et ayant le périmètre le plus petit.

"""

################################################################################

def start_list(QuerySet):

    """
        Aller chercher toutes les addresses d'un user et les mettre dans une liste
        'start_list'
    """
    list_of_addresses = []

    for user_address in QuerySet:
        address = {
                "address": user_address['name'],
                "start": user_address['start'],
                "stop": user_address['stop'],
                "distance": 0,
                "longitude": user_address['longitude'],
                "latitude": user_address['latitude']
        }

        start_list = list_of_addresses.append(address)
    
    for address in list_of_addresses:
        if address['start'] == False and address['stop'] == False:
            list_of_addresses.remove(address)

    return list_of_addresses

################################################################################

def change_reference_points(start_list):

    """
        Ensuite on change le referentiel des coordonnées de chaque adresse par
        rapport a l'adresse de départ qui a pour nouveau referentiel
        longitude = 0 et latitude = 0
    """
    reference_longitude = 0
    reference_latitude = 0

    for address in start_list:
        if address['start'] == True:
            reference_longitude = address['longitude'] 
            reference_latitude = address['latitude']

    for address in start_list:
        address['longitude'] = address['longitude'] - reference_longitude

    for address in start_list:
        address['latitude'] = address['latitude'] - reference_latitude

    return start_list

################################################################################

def calculate_distance(start_list):

    """
        Maintenant on calcule les distances des address par rapport au point de
        reference voulu.
    """
    for address in start_list:
        if address['stop'] == True:
            address['distance'] = math.sqrt(
                (address['longitude']*address['longitude']) + (address['latitude']*address['latitude'])
            )

    return start_list

################################################################################

def sorted_start_list(start_list):

    """
        Maintenant on trie la list en mettant l'adresse de debut en premier
        l'addresse de fin en dernier et entre les addresses de stop de la
        plus eloignée de l'addresse de depart a l'addresse la plus proche
    """
    the_start_place = start_list[0]
    reverse_start_list = sorted(start_list, key=lambda part: part["distance"], reverse=True)
    reverse_start_list.pop(-1)
    reverse_start_list.insert(0, the_start_place)

    return reverse_start_list






# 3 On calcule donc les distances absolue entre tout les points par rapport a l'addresse de départ grace a Pythagore
# on creer donc une fonction qui vas se charger de changer le referentiel que l'on va reutiliser a chaque fois fois

# 4 On les tris de la plus grande a la plus petite en commencant par mettre l'adresse de depart le tout dans une liste

# 5 on peut maintenant commencer notre algo decrit plus haut