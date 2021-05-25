#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpRequest
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

from address.models import Address
from address.utilities import address_tools
from bestway.models import User
from bestway.utilities import bw_tools, algorithm
from bestway.form import *

from itertools import permutations


"""

"""

################################################################################
#####                                VIEWS                                 #####
################################################################################


class SignUpView(CreateView):
    """
        This view allows the user to login or create an account.
    """
    form_class = AccountForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

@login_required
def account(request):
    """
        This view allows the user to login or create an account.
    """
    return render(request, 'account.html')

def home(request):
    """
        This view allows the user to login or create an account.
    """
    if request.method == 'POST':
        address_form = AddressForm(request.POST)

        if address_form.is_valid():
            start = bw_tools.clean_address(address_form.cleaned_data['start'])
            end = bw_tools.clean_address(address_form.cleaned_data['end'])
            start_json = bw_tools.request_to_GeoApiGouvFr(start, 'start')
            end_json = bw_tools.request_to_GeoApiGouvFr(end, 'end')

            Address.objects.filter(user_id=request.user.id, start=True).delete()
            Address.objects.filter(user_id=request.user.id, end=True).delete()

            address_tools.create_address_object(
                start_json,
                User.objects.get(id=request.user.id)
            )
            address_tools.create_address_object(
                end_json,
                User.objects.get(id=request.user.id)
            )

            return redirect('destinations')

    else:
        address_form = AddressForm()

    return render(request, 'home.html', {"address_form": address_form})

@login_required
def destinations(request):
    """
        This view allows the user to login or create an account.
    """
    if request.method == 'POST':
        stops_form = StopsForm(request.POST)

        if stops_form.is_valid():
            stop = bw_tools.clean_address(stops_form.cleaned_data['stops'])
            stop_json = bw_tools.request_to_GeoApiGouvFr(stop, 'stop')
            number_of_stop = address_tools.create_address_object(
                stop_json,
                User.objects.get(id=request.user.id)
            )

            if number_of_stop == 5:
                return redirect('result')
            else:
                pass

    else:
        stops_form = StopsForm()

    return render(request, 'destinations.html', {"stops_form": stops_form})

@login_required
def result(request):
    """
        This view allows the user to login or create an account.
    """
    id_user = int(request.user.id)
    list_of_addresses = Address.objects.filter(user_id=id_user).values()
    list_of_addresses = algorithm.addresses_list(list_of_addresses)
    ways = algorithm.find_all_differents_ways(
        list_of_addresses, len(list_of_addresses)-2
    )

    mirrors_ways = []
    mirrors_ways.append(ways)
    mirrors_ways.append(ways)

    for mirror in mirrors_ways:
        for list_of_ways in mirror:
            for addresses in list_of_ways:
                index = list_of_ways.index(addresses)
                for key, value in addresses.items():
                    if key == 'start' and value == True:
                        address_object = Address.objects.get(
                            name=addresses['address'], start=True
                        )
                        address = {
                            "address": address_object.name,
                            "nature": 'start',
                            "longitude": address_object.longitude,
                            "latitude": address_object.latitude,
                            "distance": 0
                        }
                        list_of_ways[index] = address

                    elif key == 'end' and value == True:
                        address_object = Address.objects.get(
                            name=addresses['address'], end=True
                        )
                        address = {
                            "address": address_object.name,
                            "nature": 'end',
                            "longitude": address_object.longitude,
                            "latitude": address_object.latitude,
                            "distance": 0
                        }
                        list_of_ways[index] = address

                    elif key == 'stop' and value == True:
                        address_object = Address.objects.get(
                                            name=addresses['address'], stop=True
                                        )
                        address = {
                            "address": address_object.name,
                            "nature": 'stop',
                            "longitude": address_object.longitude,
                            "latitude": address_object.latitude,
                            "distance": 0
                        }
                        list_of_ways[index] = address

    all_ways = algorithm.calculate_distances(mirrors_ways)

    the_bestway = algorithm.find_the_bestway(all_ways)

    Address.objects.filter(user_id=request.user.id).delete()

    return render(request, 'result.html', {
        'start': [the_bestway[0]],
        'stops': the_bestway[1:-1],
        'end': [the_bestway[-1]]
        }
    )

def conditions(request):
    """
        This view allows the user to login or create an account.
    """
    return render(request, 'conditions.html')

def mentions_legales(request):
    """
        This view allows the user to login or create an account.
    """
    return render(request, 'mentions_legales.html')
