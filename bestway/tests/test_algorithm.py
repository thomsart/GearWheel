#!/usr/bin/env python3
# -*- coding: utf-8 -*

import pytest

from django.test import TestCase

from bestway.utilities.algorithm import *

"""
    This file contains all tests of the functions in algorithm.py.
"""
################################################################################
#####                               Tests                                  #####
################################################################################

class TestViews(TestCase):

    def  setUp(self):
        """ We defined here all the datas we need to do our tests. """

    self.good_addresses = ""

    self.bad_addresses = ""

    self.good_addresses_list = ""

    self.bad_addresses_list = ""

    self.good_twins_of_ways = ""

    self.bad_twins_of_ways = ""

    self.good_list_of_ways_with_distances = ""

    self.bad_list_of_ways_with_distances = ""


    def test_address_list(self):
        """
            Here we test
        """
        assert addresses_list(self.good_addresses) == ""
        assert addresses_list(self.bad_addresses) == ""

    def test_find_all_differents_ways(self):
        """
            Here we test
        """
        assert find_all_differents_ways(self.good_addresses_list, 2) == ""
        assert find_all_differents_ways(self.bad_addresses_list, 2) == ""

    def test_calculate_distances(self):
        """
            Here we test
        """
        assert calculate_distances(self.good_twins_of_ways) == ""
        assert calculate_distances(self.bad_twins_of_ways) == ""
    
    def test_find_the_bestway(self):
        """
            Here we test
        """
        assert calculate_distances(self.good_list_of_ways_with_distances) == ""
        assert calculate_distances(self.bad_list_of_ways_with_distances) == ""

################################################################################