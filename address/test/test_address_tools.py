#!/usr/bin/env python3
# -*- coding: utf-8 -*

import pytest

import requests

from django.test import TestCase

from bestway.models import User
from address.utilities.address_tools import * 

"""
    This file contains all tests of the functions in address_tools.py.
"""
################################################################################
#####                               Tests                                  #####
################################################################################

class TestViews(TestCase):

    def  setUp(self):
        """ We defined here all the datas we need to do our tests. """

        self.user_login = User.objects._create_user(
            username='Ozzy',
            first_name='Jhon',
            last_name='Osbourne',
            email='crazytrain@gmail.com',
            password='PrinceOfDarknesssince1969',
            is_staff=False,
            is_active=True,
        )

        self.address_json = {
            "type": "FeatureCollection",
            "version": "draft",
            "features": [
                {
                    "type": "Feature",
                    "geometry": {
                        "type": "Point",
                        "coordinates": [
                            2.383188,
                            48.850161
                        ]
                    },
                    "properties": {
                        "label": "186 Rue du Faubourg Saint-Antoine 75012 Paris",
                        "score": 0.9807518181818181,
                        "housenumber": "186",
                        "id": "75112_3514_00186",
                        "name": "186 Rue du Faubourg Saint-Antoine",
                        "postcode": "75012",
                        "citycode": "75112",
                        "x": 654737.06,
                        "y": 6861301.09,
                        "city": "Paris",
                        "district": "Paris 12e Arrondissement",
                        "context": "75, Paris, Île-de-France",
                        "type": "housenumber",
                        "importance": 0.78827,
                        "street": "Rue du Faubourg Saint-Antoine"
                    }
                },
                {
                    "type": "Feature",
                    "geometry": {
                        "type": "Point",
                        "coordinates": [
                            2.382285,
                            48.85053
                        ]
                    },
                    "properties": {
                        "label": "Rue du Faubourg Saint-Antoine 75011 Paris",
                        "score": 0.8042155980861244,
                        "id": "75111_3514",
                        "name": "Rue du Faubourg Saint-Antoine",
                        "postcode": "75011",
                        "citycode": "75111",
                        "x": 654671.12,
                        "y": 6861342.64,
                        "city": "Paris",
                        "district": "Paris 11e Arrondissement",
                        "context": "75, Paris, Île-de-France",
                        "type": "street",
                        "importance": 0.79374
                    }
                }
            ],
            "attribution": "BAN",
            "licence": "ETALAB-2.0",
            "query": "186 rue du faubourg saint antoine paris",
            "limit": 5
        }

    def test_create_address_object(self):
        """
            Here we test
        """
        assert create_address_object(self.address_json, self.user_login) ==
    
    def test_delete_user_addresses(self):
        """
            Here we test
        """
        assert delete_user_addresses(self.user_login) ==
