#!/usr/bin/env python3
# -*- coding: utf-8 -*

import pytest
import requests

from django.test import TestCase

from bestway.utilities.bw_tools import * 

"""
    This file contains the test of the bw_tool.py.
"""

################################################################################
#####                               Tests                                  #####
################################################################################

class TestViews(TestCase):

    def  setUp(self):
        """
            We create the differents variables we need to our test.
        """

        self.good_string = "186 rue du Faubourg Saint Antoine 75012 Paris"

        self.upper_string = "186 RUE DU FAUBOURG SAINT ANTOINE 75012 PARIS"

        self.symbole_string = "'èäâê%?!^¨$,/._#²éù~µ€><£¤``()}{[]-*ç;§@àé&"

        self.empty_string = ""

    def test_clean_address(self):
        """
            Here we try to cover all differents cases of entry-texts we can get and make sure to
            obtain all those expected results to make the request to the API a success.
        """

        assert clean_address(self.good_string) == "186+rue+du+faubourg+saint+antoine+75012+paris"
        assert clean_address(self.upper_string) == "186+rue+du+faubourg+saint+antoine+75012+paris"
        assert clean_address(self.symbole_string) == "'++++++++++++++++++++++++++++++++++++++++++"
        assert clean_address(self.empty_string) == ""