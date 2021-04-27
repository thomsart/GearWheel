#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pytest

from django.test import TestCase, Client
from django.urls import reverse


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

        self.client = Client()

        return super().setUp()

    def test_home(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemlateUsed(response, 'home.html')