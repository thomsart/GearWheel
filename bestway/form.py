#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from django import forms

from django.contrib.auth.forms import forms, UserCreationForm, UserChangeForm
from django.core import validators

from bestway.models import User


# Create your models here.

class AccountForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'email',)

class LoginForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'password')

class AddressForm(forms.Form):
    start = forms.CharField(label="Départ ", max_length=70)
    end = forms.CharField(label="Arrivée ", max_length=70)

class StopsForm(forms.Form):
    stops = forms.CharField(label="Rentre tes arrêts ", max_length=70)