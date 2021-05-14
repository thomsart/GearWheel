#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
from itertools import permutations


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

def addresses_list(QuerySet):

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
                "end": user_address['end'],
                "distance": 0,
                "longitude": user_address['longitude'],
                "latitude": user_address['latitude']
        }

        list_of_addresses.append(address)

    return list_of_addresses

################################################################################

def find_all_differents_ways(addresses_list, nb_of_stops):

    start_address = [start_address for start_address in addresses_list if start_address['start']==True]
    end_address = [end_address for end_address in addresses_list if end_address['end']==True]

    for address in addresses_list:
        if address['start'] == True:
            addresses_list.remove(address)
    for address in addresses_list:
        if address['end'] == True:
            addresses_list.remove(address)

    all_permutations = [permutation for permutation in permutations(addresses_list, nb_of_stops)]

    all_combinations = []
    for permutation in all_permutations:
        permutation = list(permutation)
        all_combinations.append(permutation)

    for combination in all_combinations:
        combination.insert(0, start_address[0])
        combination.append(end_address[0])

    return all_combinations

################################################################################

def change_reference_points(addresses_list):

    """
        Ensuite on change le referentiel des coordonnées de chaque adresse par
        rapport a l'adresse de départ qui a pour nouveau referentiel
        longitude = 0 et latitude = 0
    """
    reference_longitude = 0
    reference_latitude = 0

    for address in addresses_list:
        if address['start'] == True:
            reference_longitude = address['longitude'] 
            reference_latitude = address['latitude']

    for address in addresses_list:
        address['longitude'] = address['longitude'] - reference_longitude

    for address in addresses_list:
        address['latitude'] = address['latitude'] - reference_latitude

    return addresses_list

################################################################################

def calculate_distance(addresses_list):

    """
        Maintenant on calcule les distances des address par rapport au point de
        reference voulu.
    """
    for address in addresses_list:
        if address['stop'] == True:
            address['distance'] = math.sqrt(
                (address['longitude']*address['longitude']) + (address['latitude']*address['latitude'])
            )

    return addresses_list

################################################################################

def sorted_by_distance(addresses_list):

    """
        Maintenant on trie la list en mettant l'adresse de debut en premier
        et les addresses de stop de la plus eloignée de l'addresse de depart
        à l'addresse la plus proche.
    """
    reverse_addresses_list = sorted(
                                addresses_list,
                                key=lambda part: part["distance"],
                            )

    return reverse_addresses_list

################################################################################

