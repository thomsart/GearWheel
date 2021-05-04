#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

import requests
import json

"""
    This file contains all functions we need in the views.
"""
################################################################################
#####                               Tools                                  #####
################################################################################

def create_json():

    quantity_of_json = 0

    for file in os.listdir("json"):
        quantity_of_json += 1

    datas = {
        "address": "",
        "longitude": 0,
        "latitude": 0
    }

    with open("json/stop"+str(((quantity_of_json - 3)+1))+".json", "w") as file:
        json.dump(datas, file)

    return

def main():

    create_json()

    return

if __name__ == "__main__":

    main()


