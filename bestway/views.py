#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests

from django.shortcuts import render

# Create your views here.

def home(request):

    return render(request, 'home.html')