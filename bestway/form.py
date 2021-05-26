#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from django import forms

from django.contrib.auth.forms import forms, UserCreationForm, UserChangeForm

from bestway.models import User

"""
    All the forms we need to allow the user to interacts with the Bestway
    application.
"""

class AccountForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'email',)

class LoginForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'password')

class AddressForm(forms.Form):
    """
        The form of the start and end addresses.
    """
    start = forms.CharField(label="Départ ", max_length=70)
    end = forms.CharField(label="Arrivée ", max_length=70)

class StopsForm(forms.Form):
    """
        The form of the stops and addresses.
    """
    stops = forms.CharField(label="Rentre tes arrêts ", max_length=70)