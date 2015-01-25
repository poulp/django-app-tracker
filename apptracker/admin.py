# coding: utf-8
from django.contrib import admin

from .models import Project, Issue

admin.site.register(Project)
admin.site.register(Issue)