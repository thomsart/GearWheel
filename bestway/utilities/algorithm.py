#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
from itertools import permutations


"""
    This module contains the functions we need to calculate the shortest way. 
"""

################################################################################
#####                            Algorithm                                 #####
################################################################################

def addresses_list(QuerySet):
    """
        This function takes all the addresses that the user saved to make them
        in a list, in first place, that this function returns.
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
    """
        Them this function takes the start address and the final address to put
        them in the begining and the end of each differents combinations and them
        find all the differentes combinations we can get with all the stops the
        user saved. This function return all the differente combination in a list. 
    """

    start_address = [
        start_address for start_address in addresses_list 
        if start_address['start'] == True
    ]
    end_address = [
        end_address for end_address in addresses_list 
        if end_address['end'] == True
    ]

    for address in addresses_list:
        if address['start'] == True:
            index = addresses_list.index(address)
            del addresses_list[index]
    for address in addresses_list:
        if address['end'] == True:
            index = addresses_list.index(address)
            del addresses_list[index]

    all_permutations = [
        permutation for permutation in permutations(
            addresses_list, nb_of_stops
        )
    ]

    all_combinations = []
    for permutation in all_permutations:
        permutation = list(permutation)
        all_combinations.append(permutation)

    for combination in all_combinations:
        combination.insert(0, start_address[0])
        combination.append(end_address[0])

    return all_combinations

################################################################################

def calculate_distances(twins_of_all_ways):
    """
        Now we use this function to calculate all the distances from an address
        to an other in making a mirror of the list we got from the previews
        function. The idea is to substract the longitude and latitudes of the
        first list in taking these same parameters of the preview address in the
        mirrors list. To calculate the distance between to addresses the idea is
        in fact to substract the longitude and latitude of the preview address to
        obtain a rectangle triangle and be able to calculate the hypotenuse which
        is actually the distance between to addresses. In substracting the
        longitude and latitude we put the references of the second address in
        zero. This function return the first list of thes twins of list with all
        distances we need.
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
                each_address['distance'] = math.sqrt(
                    (
                        (each_address['longitude'] - (list_of_ways_twin[index_way][index_address - 1]['longitude']))
                            *
                        (each_address['longitude'] - (list_of_ways_twin[index_way][index_address - 1]['longitude']))
                    )
                        +
                    (
                        (each_address['latitude'] - list_of_ways_twin[index_way][index_address - 1]['latitude'])
                            *
                        (each_address['latitude'] - list_of_ways_twin[index_way][index_address - 1]['latitude'])
                    )
                )

    return list_of_ways

################################################################################

def find_the_bestway(list_of_ways_with_distances):
    """
        Now that we get all distances between addresses we can thanks to this
        function simply additionate them and put the result in a dictionnary.
        We associate in each dictionnary the way and its totale distance.
        Once  we get all ways and their total distance we pick-up the shortest
        one to return it.
    """

    all_differents_ways = []
    for way in list_of_ways_with_distances:
        result = {
            'way': [],
            'total_distance': 0
        }
        for address in way:
            result['way'].append(address['address'])
            result['total_distance'] += address["distance"]
        all_differents_ways.append(result)

    indice = []
    for ways in all_differents_ways:
        indice.append(ways['total_distance'])
    distance_min = min(indice)
    the_bestway = []
    for way in all_differents_ways:
        if way['total_distance'] == distance_min:
            the_bestway.append(way['way'])

    return the_bestway[0]
