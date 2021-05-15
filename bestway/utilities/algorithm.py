#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
from itertools import permutations


"""

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

    original_addresses_list = addresses_list.copy()

    for original_way in original_addresses_list:
        ref_longitude = 0
        ref_latitude = 0
        way_indice = original_addresses_list.index(original_way)
        for address in original_way:
            ref_longitude = address['longitude']
            ref_latitude = address['latitude']

            for way in addresses_list:
                if addresses_list.index(way) == way_indice:
                    for address in way:
                        if address['start'] == False:
                            address['longitude'] -= ref_longitude
                            address['latitude'] -= ref_latitude
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

