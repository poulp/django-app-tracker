#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from django.shortcuts import render


def home(request):
    return render(request, "apptracker/general/index.html", {})