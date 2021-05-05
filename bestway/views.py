#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests

from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpRequest
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

from bestway.models import User
from address.models import Address
from bestway.form import *

# Create your views here.

class SignUpView(CreateView):
    """
        This view allows the user to login or create an account.
    """
    form_class = AccountForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

@login_required
def account(request):
     return render(request, 'account.html')

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

@login_required
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

@login_required
def result(request):

    return render(request, 'result.html')

def mentions_legales(request):

    return render(request, 'mentions_legales.html')