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

def calculate_total_distance(addresses_list):

    """
        Ensuite on change le referentiel des coordonnées de chaque adresse par
        rapport a l'adresse de départ qui a pour nouveau referentiel
        longitude = 0 et latitude = 0
    """
    curent_ref_longitude = 0
    curent_ref_latitude = 0
    next_turn_ref_longitude = 0
    next_turn_ref_latitude = 0

    for addresses in addresses_list:
        for address in addresses:
            if address['start'] == True:
                curent_ref_longitude = address['longitude'] 
                curent_ref_latitude = address['latitude']
            else:
                next_turn_ref_longitude += address['longitude']
                next_turn_ref_latitude += address['latitude']
                address['longitude'] -= curent_ref_longitude
                address['latitude'] -= curent_ref_latitude
                address['distance'] = math.sqrt(
                        (address['longitude']*address['longitude']) + (address['latitude']*address['latitude'])
                    )

    return addresses_list

################################################################################

def total_distance_for_each_way(addresses_list):

    """
        Maintenant on calcule les distances des address par rapport au point de
        reference voulu.
    """
    list_for_comparison = []

    for way in addresses_list:
        indices = {
                "bestway": [],
                "total_distance": 0
            }
        for address in way:
            if address['start'] == True:
                indices["bestway"].append(address['address'])
            else:
                indices["bestway"].append(address['address'])
                indices["total_distance"] += address['distance']
        list_for_comparison.append(indices)

    return list_for_comparison

################################################################################

