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

BESTWAY_GOOGLEMAP_KEY = os.environ['BESTWAY_GOOGLEMAP_KEY']

def main():

    keep_caracters = [
        '0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h',
        'i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
        "'"
        ]
    address = input("le point de départ : \n")
    address = address.lower()
    for caracter in address:
        if caracter in keep_caracters:
            continue
        else:
            address = address.replace(caracter, "+")

    print(address)

    response = requests.get("https://api-adresse.data.gouv.fr/search/?q="+address)
    
    print("Adresse : "+response.json()['features'][0]['properties']['label'])
    print("Longitude : "+str(response.json()['features'][0]['geometry']['coordinates'][0]))
    print("Latitude : "+str(response.json()['features'][0]['geometry']['coordinates'][1]))

    return

if __name__ == "__main__":

    main()


