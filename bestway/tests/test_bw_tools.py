#!/usr/bin/env python3
# -*- coding: utf-8 -*

import pytest

from django.test import TestCase

from bestway.utilities.bw_tools import * 

"""
    This file contains all tests of the functions in bw_tools.py.
"""
################################################################################
#####                               Tests                                  #####
################################################################################

class TestViews(TestCase):

    def  setUp(self):
        """ We defined here all the datas we need to do our tests. """

        self.good_string = "186 rue du Faubourg Saint Antoine 75012 Paris"

        self.upper_string = "186 RUE DU FAUBOURG SAINT ANTOINE 75012 PARIS"

        self.symbole_string = "'èäâê%?!^¨$,/._#²éù~µ€><£¤``()}{[]-*ç;§@àé&"

        self.empty_string = ""

    def test_clean_address(self):
        """
            Here we test
        """

        assert clean_address(self.good_string) == "186+rue+du+faubourg+saint+antoine+75012+paris"
        assert clean_address(self.upper_string) == "186+rue+du+faubourg+saint+antoine+75012+paris"
        assert clean_address(self.symbole_string) == "'++++++++++++++++++++++++++++++++++++++++++"
        assert clean_address(self.empty_string) == ""

    # def request_to_GeoApiGouvFr(self):
    #     """
    #         Here we test 
    #     """

    #     assert tools.put_products_in_db(self.dict_without_product) == False

################################################################################