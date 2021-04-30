#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests

from django.shortcuts import render
from django.http import HttpResponseRedirect

from bestway.form import *

# Create your views here.

def home(request):

    if request.method == 'POST':
        address_form = AddressForm(request.POST)
        if address_form.is_valid():
            addresses = [
                address_form.cleaned_data['address_start'],
                address_form.cleaned_data['address_end']
            ]
            print(addresses)

            return HttpResponseRedirect('')

    else:
        address_form = AddressForm()

    return render(request, 'home.html', {"address_form": address_form})


def mentions_legales(request):

    return render(request, 'mentions_legales.html')