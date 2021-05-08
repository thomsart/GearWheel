#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import requests

from address.models import Address
from bestway.models import User


"""
    This file contains all functions we need in the views.
"""
################################################################################
#####                               Tools                                  #####
################################################################################

def clean_address(address):

    """
        This function formate the address that the user enter in the form in
        oder to make the requests success in the API. 
    """
    caracters_to_keep = [
        '0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h',
        'i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
        "'"
    ]
    address = address.lower()
    for caracter in address:
        if caracter in caracters_to_keep:
            continue
        else:
            address = address.replace(caracter, "+")

    return address

################################################################################

def request_to_GeoApiGouvFr(address, nature):

    """
        This function will request to 'https://geo.api.gouv.fr/adresse',
        in order to get the good syntaxe of the address and its coorinates.
    """
    response = requests.get("https://api-adresse.data.gouv.fr/search/?q="+address)

    print(response)

    address = response.json()['features'][0]['properties']['label']
    longitude = str(response.json()['features'][0]['geometry']['coordinates'][0])
    latitude = str(response.json()['features'][0]['geometry']['coordinates'][1])

    return {
        "address": address,
        "nature": nature,
        "longitude": longitude,
        "latitude": latitude
    }

################################################################################

def create_address_object(json_address, user_logged_id):

    """
        This function will create the address object for the user how is logged
        in order to take it later to make our calculation of the shotest way.
        We just precise in argument if the address is the start, the end or just
        a stop.
    """

    if json_address['nature']=='start':
        Address.objects.create(
                    name = json_address['address'],
                    longitude = float(json_address['longitude']),
                    latitude = float(json_address['latitude']),
                    start = True,
                    end = False,
                    stop = False,
                    user = user_logged_id
                )

    elif json_address['nature']=='end':
        Address.objects.create(
                    name = json_address['address'],
                    longitude = float(json_address['longitude']),
                    latitude = float(json_address['latitude']),
                    start = False,
                    end = True,
                    stop = False,
                    user = user_logged_id
                )

    elif json_address['nature']=='stop':
        Address.objects.create(
                    name = json_address['address'],
                    longitude = float(json_address['longitude']),
                    latitude = float(json_address['latitude']),
                    start = False,
                    end = False,
                    stop = True,
                    user = user_logged_id
                )

    else:
        return print("Il faut renseigner la nature du trajet : 'start', 'end' ou 'stop'")    

################################################################################

def check_if_request_is_good():

    pass

################################################################################
