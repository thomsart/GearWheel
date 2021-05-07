#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pytest

from django.test import TestCase, Client
from django.urls import reverse

from bestway.models import User


"""
    In this file we test all our views in the 'bestway' application in asserting
    of the used templates, the requests code or the urls redirections.
"""

################################################################################
#####                             Tests                                    ##### 
################################################################################

class TestViews(TestCase):

    def setUp(self):
        """ We defined here all the datas we create to do our tests. """

        #self.csrf_client = Client(enforce_csrf_checks=True)

        self.client = Client()

        self.user_signup = {
            'username': 'Jojo',
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

        return super().setUp()

    def test_home(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

    def test_signup(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/signup.html')

    def test_signup_success(self):
        response = self.client.post(reverse('signup'), self.user_signup,
                                    format='text/html')
        self.assertEqual(response.status_code, 302)

    def test_login(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/login.html')

    def test_login_success(self):
        response = self.client.post(reverse('login'),
                                    {'username': 'Jojo',
                                    'password': 'ThePassword77+'})
        self.assertEqual(response.status_code, 302)

    def test_account(self):
        self.client.force_login(self.user_login)
        response = self.client.get(reverse('account'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'account.html')

    # def test_destinations(self):
    #     response = self.client.post(reverse('destinations'))
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'destinations.html')

    # def test_result(self):
    #     response = self.client.get(reverse('result'))
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'result.html')

    def test_mentions_legales(self):
        response = self.client.get(reverse('mentions_legales'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'mentions_legales.html')