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

def take_all_longitude_and_latitude(addresses_list):

    """
        Ensuite on change le referentiel des coordonnées de chaque adresse par
        rapport a l'adresse de départ qui a pour nouveau referentiel
        longitude = 0 et latitude = 0
    """

    longitude = []
    latitude = []
    longitude2 = []
    latitude2 = []

    original_addresses_list = addresses_list

    for original_way in original_addresses_list:
        way_indice = original_addresses_list.index(original_way)
        for original_address in original_way:
            original_address_indice = original_way.index(original_address)
            longitude.append(original_address['longitude'])
            latitude.append(original_address['latitude'])

            for way in addresses_list:
                if addresses_list.index(way) == way_indice:
                    for address in way:
                        if way.index(address) == original_address_indice + 1 :
                            longitude2.append(address['longitude'])
                            latitude2.append(address['latitude'])
                            if address['end'] == True:
                                longitude.append("LONG")
                                longitude2.append("LONG2")
                                latitude.append("LAT")
                                latitude2.append("LAT2")

    return [longitude, longitude2, latitude, latitude2]

################################################################################

def total_distance_for_each_way(addresses_list, coordinates):

    """
        Maintenant on calcule les distances des address par rapport au point de
        reference voulu.
    """
    coordinates
    list_for_comparison = []

    for way in addresses_list:
        indices = {
                "bestway": [],
                "total_distance": []
            }
        for address in way:
            if address['start'] == True:
                indices["bestway"].append(address['address'])
            else:
                indices["bestway"].append(address['address'])
                indices["total_distance"].append(address['distance'])
            list_for_comparison.append(indices)

    return list_for_comparison

################################################################################

