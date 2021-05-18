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
        }

        list_of_addresses.append(address)

    return list_of_addresses

################################################################################

def find_all_differents_ways(addresses_list, nb_of_stops):

    start_address = [start_address for start_address in addresses_list if start_address['start']==True]
    end_address = [end_address for end_address in addresses_list if end_address['end']==True]

    for address in addresses_list:
        if address['start'] == True:
            index = addresses_list.index(address)
            del addresses_list[index]
    for address in addresses_list:
        if address['end'] == True:
            index = addresses_list.index(address)
            del addresses_list[index]

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

def instance_two_times_all_ways_list(all_combinations):

    all_combinations

    object = {
        "address": "",
        "nature": "start",
        "longitude": 0,
        "latitude": 0,
        "distance": 0
    }

    # instancier ici la liste deux fois

    return [[[object, object], [object, object]], [[object, object], [object, object]]]

################################################################################

def calculate_distances(twins_of_all_ways):

    """
        
    """
    list_of_ways = twins_of_all_ways[0]
    list_of_ways_twin = twins_of_all_ways[1]

    for each_way in list_of_ways:
        index_way = list_of_ways.index(each_way)
        for each_address in each_way:
            if each_address['nature'] == 'start':
                continue
            else:
                index_address = each_way.index(each_address)
                each_address["distance"] = math.sqrt(
                    (
                        (each_address['long'] - (list_of_ways_twin[index_way][index_address - 1]['long']))
                            *
                        (each_address['long'] - (list_of_ways_twin[index_way][index_address - 1]['long']))
                    )
                        +
                    (
                        (each_address['lat'] - list_of_ways_twin[index_way][index_address - 1]['lat'])
                            *
                        (each_address['lat'] - list_of_ways_twin[index_way][index_address - 1]['lat'])
                    )
                )

    return list_of_ways

################################################################################

def find_the_bestway(list_of_ways_with_distances):

    """
        Maintenant on calcule les distances des address par rapport au point de
        reference voulu.
    """

    the_bestway_way = []

    for way in list_of_ways_with_distances:
        result = {
            'way': [],
            'total_distance': 0
        }
        for address in way:
            result['way'].append(address['address'])
            result['total_distance'] += address["distance"]

        the_bestway_way.append(result)

    return the_bestway_way

################################################################################
