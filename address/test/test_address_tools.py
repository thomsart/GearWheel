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
        """
            We defined here all the variables we need to do our tests.
        """

        self.user_login = User.objects._create_user(
            username='Ozzy',
            first_name='Jhon',
            last_name='Osbourne',
            email='crazytrain@gmail.com',
            password='PrinceOfDarknesssince1969',
            is_staff=False,
            is_active=True,
        )

        self.start_address = {
            'address': '186 Rue du Faubourg Saint-Antoine 75012 Paris', 
            'nature': 'start', 
            'longitude': '2.383188', 
            'latitude': '48.850161'
        }

        self.end_address = {
            'address': '186 Rue du Faubourg Saint-Antoine 75012 Paris', 
            'nature': 'end', 
            'longitude': '2.383188', 
            'latitude': '48.850161'
        }

        self.stop_address = {
            'address': '11 rue des templiers la Croix en Brie', 
            'nature': 'stop', 
            'longitude': '2.383188', 
            'latitude': '48.850161'
        }

################################################################################

    def test_create_address_object(self):
        """
            Here we test that the creation of the three addresses works in using
            the function create_address_object().
        """
        create_address_object(self.start_address, self.user_login)
        create_address_object(self.end_address, self.user_login)
        create_address_object(self.stop_address, self.user_login)
        new_addresses_in_db = Address.objects.count()

        assert new_addresses_in_db == 3

################################################################################