#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from django.contrib import admin

from .models import Project, Issue, Label


admin.site.register(Project)
admin.site.register(Issue)
admin.site.register(Label)