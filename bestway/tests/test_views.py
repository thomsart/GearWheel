#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pytest

from django.test import TestCase, Client
from django.urls import reverse

from bestway.form import AddressForm


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

        self.start_end = [
            {
                'start': 'Paris',
                'end': 'Milan'
            }
        ]

        self.form = AddressForm(self.start_end)

        return super().setUp()

    def test_home(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

    def test_destinations_with_datas_in_body(self):
        response = self.client.post(reverse('destinations', args=self.form))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'destinattions.html')

    def test_destinations_without_datas_in_body(self):
        response = self.client.get(reverse('destinations', args={}))
        self.assertEqual(response.status_code, 404)
        self.assertTemplateUsed(response, 'destinattions.html')

    def test_mentions_legales(self):
        response = self.client.get(reverse('mentions_legales'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'mentions_legales.html')