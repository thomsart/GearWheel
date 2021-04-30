#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests

from django.shortcuts import render
from django.shortcuts import redirect

from bestway.form import *

# Create your views here.

def home(request):

    if request.method == 'POST':
        address_form = AddressForm(request.POST)
        if address_form.is_valid():
            start_end = [
                address_form.cleaned_data['address_start'],
                address_form.cleaned_data['address_end']
            ]
            return redirect('destinations', {"start_end": start_end})

    else:
        address_form = AddressForm()

    return render(request, 'home.html', {"address_form": address_form})

def destinations(request, start_end):

    return render(request, 'destinations.html')

def mentions_legales(request):

    return render(request, 'mentions_legales.html')