#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from address.models import Address

"""
    This file contains all functions we need in the views.
"""
################################################################################
#####                               Tools                                  #####
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

def delete_user_addresses(id_user):
    Address.objects.filter(user_id=id_user).delete()
    return