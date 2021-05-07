#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import requests



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

def request_to_GeoApiGouvFr(address):

    """
        This function will request to 'https://geo.api.gouv.fr/adresse',
        in order to get the good syntaxe of the address and its coorinates.
    """
    response = requests.get("https://api-adresse.data.gouv.fr/search/?q="+address)

    address = response.json()['features'][0]['properties']['label']
    longitude = str(response.json()['features'][0]['geometry']['coordinates'][0])
    latitude = str(response.json()['features'][0]['geometry']['coordinates'][1])

    return {
        "address": address,
        "longitude": longitude,
        "latitude": latitude
    }

################################################################################

def check_if_request_is_good():

    pass

################################################################################
