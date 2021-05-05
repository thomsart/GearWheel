#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests

from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpRequest

from bestway.form import *
from user.models import User
from address.models import Address


# Create your views here.

def home(request):

    if request.method == 'POST':
        address_form = AddressForm(request.POST)

        if address_form.is_valid():
            start = address_form.cleaned_data['start']
            end = address_form.cleaned_data['end']

            print(request.POST['start'])
            print(request.POST['end'])

            return redirect('destinations')

    else:
        address_form = AddressForm()

    return render(request, 'home.html', {"address_form": address_form})

def destinations(request):

    # places = {
    #     'start': request.POST['start'],
    #     'end': request.POST['end'],
    #     'stops': []
    # }

    if request.method == 'POST':

        stops_form = StopsForm(request.POST)

        if stops_form.is_valid():
            print(stops_form.cleaned_data['stops'])
            # places['stops'].append(stops_form.cleaned_data['stops'])

    else:
        stops_form = StopForm()

    return render(request, 'destinations.html', {"stops_form": stops_form})

def result(request):

    return render(request, 'result.html')

def mentions_legales(request):

    return render(request, 'mentions_legales.html')