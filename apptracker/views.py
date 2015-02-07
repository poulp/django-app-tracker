#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from django.shortcuts import render


def index(request):
    return render(request, "apptracker/base.html", {})