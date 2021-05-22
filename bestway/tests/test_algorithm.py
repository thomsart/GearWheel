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

        self.good_queryset = [
            {'id': 23, 'name': 'départ', 'longitude': 30, 'latitude': 50, 'start': True, 'end': False, 'stop': False, 'user_id': 1},
            {'id': 24, 'name': 'arrivée', 'longitude': 10, 'latitude': 40, 'start': False, 'end': True, 'stop': False, 'user_id': 1},
            {'id': 25, 'name': 'pointA', 'longitude': 30, 'latitude': 80, 'start': False, 'end': False, 'stop': True, 'user_id': 1},
            {'id': 26, 'name': 'pointB', 'longitude': 20, 'latitude': 70, 'start': False, 'end': False, 'stop': True, 'user_id': 1},
        ]
        self.bad_queryset = [
            {'id': 25, 'name': 'pointA', 'longitude': 30, 'latitude': 80, 'start': False, 'end': False, 'stop': True, 'user_id': 1},
            {'id': 24, 'name': 'arrivée', 'longitude': 10, 'latitude': 40, 'start': False, 'end': True, 'stop': False, 'user_id': 1},
            {'id': 26, 'name': 'pointB', 'longitude': 20, 'latitude': 70, 'start': False, 'end': False, 'stop': True, 'user_id': 1},
            {'id': 23, 'name': 'départ', 'longitude': 30, 'latitude': 50, 'start': True, 'end': False, 'stop': False, 'user_id': 1},
        ]
        self.good_addresses_list = [
            {'address': 'départ', 'start': True, 'end': False, 'stop': False},
            {'address': 'arrivée', 'start': False, 'end': True, 'stop': False},
            {'address': 'pointA', 'start': False, 'end': False, 'stop': True},
            {'address': 'pointB', 'start': False, 'end': False, 'stop': True},
        ]
        self.bad_addresses_list = [
            {'address': 'pointA', 'start': False, 'end': False, 'stop': True},
            {'address': 'arrivée', 'start': False, 'end': True, 'stop': False},
            {'address': 'pointB', 'start': False, 'end': False, 'stop': True},
            {'address': 'départ', 'start': True, 'end': False, 'stop': False},
        ]

        self.twins_of_ways = [
            [
                [
                    {'address': '25 Rue de la Croix Blanche 77570 Bougligny', 'nature': 'start', 'longitude': 2.658703, 'latitude': 48.198482, 'distance': 0}, 
                    {'address': '11 Rue du Maine 75014 Paris', 'nature': 'stop', 'longitude': 2.322771, 'latitude': 48.840555, 'distance': 0}, 
                    {'address': '186 Rue du Faubourg Saint-Antoine 75012 Paris', 'nature': 'stop', 'longitude': 2.383188, 'latitude': 48.850161, 'distance': 0},  
                    {'address': 'Rue de Paris 77140 Nemours', 'nature': 'end', 'longitude': 2.693246, 'latitude': 48.26716, 'distance': 0}
                ],  
                [
                    {'address': '25 Rue de la Croix Blanche 77570 Bougligny', 'nature': 'start', 'longitude': 2.658703, 'latitude': 48.198482, 'distance': 0}, 
                    {'address': '186 Rue du Faubourg Saint-Antoine 75012 Paris', 'nature': 'stop', 'longitude': 2.383188, 'latitude': 48.850161, 'distance': 0}, 
                    {'address': '11 Rue du Maine 75014 Paris', 'nature': 'stop', 'longitude': 2.322771, 'latitude': 48.840555, 'distance': 0},  
                    {'address': 'Rue de Paris 77140 Nemours', 'nature': 'end', 'longitude': 2.693246, 'latitude': 48.26716, 'distance': 0}
                ],  
            ], 
            [
                [
                    {'address': '25 Rue de la Croix Blanche 77570 Bougligny', 'nature': 'start', 'longitude': 2.658703, 'latitude': 48.198482, 'distance': 0}, 
                    {'address': '11 Rue du Maine 75014 Paris', 'nature': 'stop', 'longitude': 2.322771, 'latitude': 48.840555, 'distance': 0}, 
                    {'address': '186 Rue du Faubourg Saint-Antoine 75012 Paris', 'nature': 'stop', 'longitude': 2.383188, 'latitude': 48.850161, 'distance': 0},  
                    {'address': 'Rue de Paris 77140 Nemours', 'nature': 'end', 'longitude': 2.693246, 'latitude': 48.26716, 'distance': 0}
                ],  
                [
                    {'address': '25 Rue de la Croix Blanche 77570 Bougligny', 'nature': 'start', 'longitude': 2.658703, 'latitude': 48.198482, 'distance': 0}, 
                    {'address': '186 Rue du Faubourg Saint-Antoine 75012 Paris', 'nature': 'stop', 'longitude': 2.383188, 'latitude': 48.850161, 'distance': 0}, 
                    {'address': '11 Rue du Maine 75014 Paris', 'nature': 'stop', 'longitude': 2.322771, 'latitude': 48.840555, 'distance': 0},  
                    {'address': 'Rue de Paris 77140 Nemours', 'nature': 'end', 'longitude': 2.693246, 'latitude': 48.26716, 'distance': 0}
                ],
            ]
        ]

        self.list_of_ways_with_distances = [
            [
                {'address': '25 Rue de la Croix Blanche 77570 Bougligny', 'nature': 'start', 'longitude': 2.658703, 'latitude': 48.198482, 'distance': 0}, 
                {'address': '11 Rue du Maine 75014 Paris', 'nature': 'stop', 'longitude': 2.322771, 'latitude': 48.840555, 'distance': 0.7246433922647777}, 
                {'address': '186 Rue du Faubourg Saint-Antoine 75012 Paris', 'nature': 'stop', 'longitude': 2.383188, 'latitude': 48.850161, 'distance': 0.061175886793735826}, 
                {'address': 'Rue de Paris 77140 Nemours', 'nature': 'end', 'longitude': 2.693246, 'latitude': 48.26716, 'distance': 0.6603227463634759}
            ], 
            [
                {'address': '25 Rue de la Croix Blanche 77570 Bougligny', 'nature': 'start', 'longitude': 2.658703, 'latitude': 48.198482, 'distance': 0}, 
                {'address': '186 Rue du Faubourg Saint-Antoine 75012 Paris', 'nature': 'stop', 'longitude': 2.383188, 'latitude': 48.850161, 'distance': 0.7075267021575947}, 
                {'address': '11 Rue du Maine 75014 Paris', 'nature': 'stop', 'longitude': 2.322771, 'latitude': 48.840555, 'distance': 0.061175886793735826}, 
                {'address': 'Rue de Paris 77140 Nemours', 'nature': 'end', 'longitude': 2.693246, 'latitude': 48.26716, 'distance': 0.6826665010457197}
            ]
        ]

################################################################################

    def test_addresses_list(self):
        """
            Here we test
        """
        assert addresses_list(self.good_queryset) == [
            {'address': 'départ', 'start': True, 'stop': False, 'end': False},
            {'address': 'arrivée', 'start': False, 'stop': False, 'end': True}, 
            {'address': 'pointA', 'start': False, 'stop': True, 'end': False}, 
            {'address': 'pointB', 'start': False, 'stop': True, 'end': False}, 
        ]
        assert addresses_list(self.bad_queryset) == [
            {'address': 'pointA', 'start': False, 'stop': True, 'end': False},
            {'address': 'arrivée', 'start': False, 'stop': False, 'end': True},
            {'address': 'pointB', 'start': False, 'stop': True, 'end': False},
            {'address': 'départ', 'start': True, 'stop': False, 'end': False},
        ]

    def test_find_all_differents_ways(self):
        """
            Here we test
        """
        assert find_all_differents_ways(self.good_addresses_list, len(self.good_addresses_list)-2) == [
            [
                {'address': 'départ', 'start': True, 'stop': False, 'end': False}, 
                {'address': 'pointA', 'start': False, 'stop': True, 'end': False}, 
                {'address': 'pointB', 'start': False, 'stop': True, 'end': False}, 
                {'address': 'arrivée', 'start': False, 'stop': False, 'end': True}
            ], 
            [
                {'address': 'départ', 'start': True, 'stop': False, 'end': False}, 
                {'address': 'pointB', 'start': False, 'stop': True, 'end': False}, 
                {'address': 'pointA', 'start': False, 'stop': True, 'end': False}, 
                {'address': 'arrivée', 'start': False, 'stop': False, 'end': True}
            ]
        ]
        assert find_all_differents_ways(self.bad_addresses_list, len(self.bad_addresses_list)-2) == [
            [
                {'address': 'départ', 'start': True, 'stop': False, 'end': False}, 
                {'address': 'pointA', 'start': False, 'stop': True, 'end': False}, 
                {'address': 'pointB', 'start': False, 'stop': True, 'end': False}, 
                {'address': 'arrivée', 'start': False, 'stop': False, 'end': True}
            ], 
            [
                {'address': 'départ', 'start': True, 'stop': False, 'end': False}, 
                {'address': 'pointB', 'start': False, 'stop': True, 'end': False}, 
                {'address': 'pointA', 'start': False, 'stop': True, 'end': False}, 
                {'address': 'arrivée', 'start': False, 'stop': False, 'end': True}
            ]
        ]

    def test_calculate_distances(self):
        """
            Here we test
        """
        assert calculate_distances(self.twins_of_ways) == [
            [
                {'address': '25 Rue de la Croix Blanche 77570 Bougligny', 'nature': 'start', 'longitude': 2.658703, 'latitude': 48.198482, 'distance': 0}, 
                {'address': '11 Rue du Maine 75014 Paris', 'nature': 'stop', 'longitude': 2.322771, 'latitude': 48.840555, 'distance': 0.7246433922647777}, 
                {'address': '186 Rue du Faubourg Saint-Antoine 75012 Paris', 'nature': 'stop', 'longitude': 2.383188, 'latitude': 48.850161, 'distance': 0.061175886793735826}, 
                {'address': 'Rue de Paris 77140 Nemours', 'nature': 'end', 'longitude': 2.693246, 'latitude': 48.26716, 'distance': 0.6603227463634759}
            ], 
            [
                {'address': '25 Rue de la Croix Blanche 77570 Bougligny', 'nature': 'start', 'longitude': 2.658703, 'latitude': 48.198482, 'distance': 0}, 
                {'address': '186 Rue du Faubourg Saint-Antoine 75012 Paris', 'nature': 'stop', 'longitude': 2.383188, 'latitude': 48.850161, 'distance': 0.7075267021575947}, 
                {'address': '11 Rue du Maine 75014 Paris', 'nature': 'stop', 'longitude': 2.322771, 'latitude': 48.840555, 'distance': 0.061175886793735826}, 
                {'address': 'Rue de Paris 77140 Nemours', 'nature': 'end', 'longitude': 2.693246, 'latitude': 48.26716, 'distance': 0.6826665010457197}
            ]
        ]
    
    def test_find_the_bestway(self):
        """
            Here we test
        """
        assert find_the_bestway(self.list_of_ways_with_distances) == [
            '25 Rue de la Croix Blanche 77570 Bougligny', 
            '11 Rue du Maine 75014 Paris', 
            '186 Rue du Faubourg Saint-Antoine 75012 Paris', 
            'Rue de Paris 77140 Nemours'
        ]

################################################################################