#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pytest

from django.test import TestCase, Client
from django.urls import reverse

from bestway.models import User
from address.models import Address

"""
    In this file we test all our views in the 'bestway' application in asserting
    of the used templates, the requests code or the urls redirections.
"""

################################################################################
#####                             Tests                                    ##### 
################################################################################

class TestViews(TestCase):

    def setUp(self):
        """
            We create all the variables we need to do our tests.
        """

        self.client = Client()

        self.user_signup = {
            'username': 'Jeanjean',
            'first_name': 'Jean',
            'email': 'grosjean@gmail.com',
            'password1': 'ThePassword1985+',
            'password2': 'ThePassword1985+',
        }

        self.user_login = User.objects._create_user(
            username='Jojo',
            first_name='Jhon',
            last_name='Doe',
            email='jhondoetheunknow@gmail.com',
            password='ThePassword77+',
            is_staff=False,
            is_active=True,
            )

        self.addresses_start = Address.objects.create(
            id=30, name='25 Rue de la Croix Blanche 77570 Bougligny', longitude=2.5,
            latitude=48, start=True, end=False, stop=False, user=self.user_login
        )

        self.addresses_end = Address.objects.create(
            id=31, name='Rue de Paris 77140 Nemours', longitude=2.7,
            latitude=48.2, start=False, end=True, stop=False, user=self.user_login
        )

        self.addresses_stop1 = Address.objects.create(
            id=32, name='11 Rue du Maine 75014 Paris', longitude=2.3,
            latitude=48.8, start=False, end=False, stop=True, user=self.user_login
        )

        self.addresses_stop2 = Address.objects.create(
            id=33, name='186 Rue du Faubourg Saint-Antoine 75012 Paris', longitude=2.4,
            latitude=48.8, start=False, end=False, stop=True, user=self.user_login
        )

        return super().setUp()

################################################################################

    def test_home(self):
        """
            We make sure that the status code is 200 and that this template is
            used in the response from our server.
        """
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

################################################################################

    def test_signup(self):
        """
            We make sure that the status code is 200 and that this template is
            used in the response from our server.
        """
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/signup.html')

################################################################################

    def test_signup_success(self):
        """
            We make sure that the status code is 302 when the user signup.
        """
        response = self.client.post(reverse('signup'), self.user_signup,
                                    format='text/html')
        self.assertEqual(response.status_code, 302)

################################################################################

    def test_login(self):
        """
            We make sure that the status code is 200 and that this template is
            used in the response from our server.
        """
    
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/login.html')

################################################################################

    def test_login_success(self):
        """
            We make sure that the status code is 302 when the logging is a
            success.
        """
        response = self.client.post(reverse('login'),
                                    {'username': 'Jojo',
                                    'password': 'ThePassword77+'})
        self.assertEqual(response.status_code, 302)

################################################################################

    def test_account(self):
        """
            We make sure that the status code is 200 and that this template is
            used in the response from our server when the user is logged.
        """
        self.client.force_login(self.user_login)
        response = self.client.get(reverse('account'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'account.html')

################################################################################

    def test_destinations(self):
        """
            We make sure that the status code is 200 and that this template is
            used in the response from our server when the user is logged.
        """
        self.client.force_login(self.user_login)
        response = self.client.get(reverse('destinations'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'destinations.html')

################################################################################

    def test_result(self):
        """
            We make sure that the status code is 200 and that this template is
            used in the response from our server when the user is logged.
        """
        self.client.force_login(self.user_login)
        response = self.client.get(reverse('result'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'result.html')

################################################################################

    def test_delete_user_addresses(self):
        """
            We make sure that the status code is 200 and that this template is
            used in the response from our server when the user is logged.
        """
        self.client.force_login(self.user_login)
        response = self.client.get(reverse('result'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'result.html')

################################################################################

    def test_conditions(self):
        """
            We make sure that the status code is 200 and that this template is
            used in the response from our server.
        """
        response = self.client.get(reverse('conditions'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'conditions.html')

################################################################################

    def test_mentions_legales(self):
        """
            We make sure that the status code is 200 and that this template is
            used in the response from our server.
        """
        response = self.client.get(reverse('mentions_legales'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'mentions_legales.html')

################################################################################
