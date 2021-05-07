#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpRequest
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

from address.models import Address
from bestway.models import User
from bestway.utilities import bw_tools
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
            start = bw_tools.clean_address(address_form.cleaned_data['start'])
            end = bw_tools.clean_address(address_form.cleaned_data['end'])
            print(start+'\n'+end)
            start_json = bw_tools.request_to_GeoApiGouvFr(start)
            end_json = bw_tools.request_to_GeoApiGouvFr(end)
            print(start_json)
            print(end_json)

            return redirect('destinations')

    else:
        address_form = AddressForm()

    return render(request, 'home.html', {"address_form": address_form})

@login_required
def destinations(request):

    if request.method == 'POST':
        stops_form = StopsForm(request.POST)

        if stops_form.is_valid():
            stop = bw_tools.clean_address(stops_form.cleaned_data['stops'])
            print(stop)
            stop_json = bw_tools.request_to_GeoApiGouvFr(stop)
            print(stop_json)

            logged_user_id = User.objects.filter(id=request.user.id).value('id')
            Address.objects.create(
                name = stop_json['address'],
                longitude = float(stop_json['longitude']),
                latitude = float(stop_json['latitude']),
                start = False,
                end = False,
                stop = True,
                user = logged_user_id
            )

    else:
        stops_form = StopsForm()

    return render(request, 'destinations.html', {"stops_form": stops_form})

@login_required
def result(request):

    return render(request, 'result.html')

def mentions_legales(request):

    return render(request, 'mentions_legales.html')