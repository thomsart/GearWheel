#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from address.models import Address

"""
    This file contains all functions we need in the views to create address
    objects.
"""

################################################################################
#####                               Tools                                  #####
################################################################################

def create_address_object(json_address, user_logged_id):
    """
        This function will create the address object for the logged user
        in order to take it later to make our calculation of the shotest way.
        We just precise in argument if the address is the start, the end or just
        a stop.
    """

    if json_address['nature'] =='start':
        Address.objects.create(
            name = json_address['address'],
            longitude = float(json_address['longitude']),
            latitude = float(json_address['latitude']),
            start = True,
            end = False,
            stop = False,
            user = user_logged_id
        )

    elif json_address['nature'] =='end':
        Address.objects.create(
            name = json_address['address'],
            longitude = float(json_address['longitude']),
            latitude = float(json_address['latitude']),
            start = False,
            end = True,
            stop = False,
            user = user_logged_id
        )

    elif json_address['nature'] =='stop':
        is_in_db = Address.objects.filter(name=json_address['address'], user_id=user_logged_id)
        if is_in_db:
            print("Tu as deja enregistré cette adesse !")
            pass
        else:
            Address.objects.create(
                name = json_address['address'],
                longitude = float(json_address['longitude']),
                latitude = float(json_address['latitude']),
                start = False,
                end = False,
                stop = True,
                user = user_logged_id
            )

    return Address.objects.filter(stop=True, user_id=user_logged_id).count()

################################################################################

