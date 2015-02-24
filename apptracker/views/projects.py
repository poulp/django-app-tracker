#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.core.urlresolvers import reverse

from apptracker.models import Project
from apptracker.mixins import LoginRequiredMixin, PermissionRequiredMixin


class ProjectListView(ListView):
    model = Project
    template_name = 'apptracker/projects/list.html'
    context_object_name = 'projects'


class ProjectCreateView(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    template_name = 'apptracker/projects/create.html'
    model = Project
    fields = [
        'name',
        'description',
        'repository',
        'documentation'
    ]
    permissions = ['apptracker.create_project']

    def get_success_url(self):
        return reverse('project-list')


class ProjectUpdateView(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    template_name = 'apptracker/projects/edit.html'
    model = Project
    pk_url_kwarg = 'project_pk'
    context_object_name = 'project'
    fields = [
        'name',
        'description',
        'repository',
        'documentation'
    ]
    permissions = ['apptracker.edit_project']

    def get_success_url(self):
        return reverse('project-list')


class ProjectDeleteView(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    model = Project
    template_name = 'apptracker/projects/confirm_delete.html'
    context_object_name = 'project'
    pk_url_kwarg = 'project_pk'
    permissions = ['apptracker.delete_project']

    def get_success_url(self):
        return reverse('project-list')