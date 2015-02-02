# coding: utf-8
from django.contrib import admin

from .models import Project, Issue, IssueActivity, Label

admin.site.register(Project)
admin.site.register(Issue)
admin.site.register(IssueActivity)
admin.site.register(Label)