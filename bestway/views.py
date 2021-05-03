#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests

from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpRequest

from bestway.form import *

# Create your views here.

def home(request):

    if request.method == 'POST':
        address_form = AddressForm(request.POST)

        if address_form.is_valid():
            return redirect('destinations', address_form.cleaned_data)

    else:
        address_form = AddressForm()

    return render(request, 'home.html', {"address_form": address_form})

def destinations(request, *args):

    start = request.POST['start']
    end = request.POST['end']
    # print(start)
    # print(end)

    return render(request, 'destinations.html')

def mentions_legales(request):

    return render(request, 'mentions_legales.html')