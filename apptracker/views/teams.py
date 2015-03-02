#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from django.core.urlresolvers import reverse

from apptracker.models import TrackerTeam
from apptracker.mixins import LoginRequiredMixin, PermissionRequiredMixin
from apptracker.forms import TrackerTeamForm


class TeamListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    template_name = 'apptracker/projects/teams/list.html'
    context_object_name = 'teams'
    permissions = ['apptracker.view_trackerteam']

    def get_queryset(self):
        return TrackerTeam.objects.all()


class TeamCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    template_name = 'apptracker/projects/teams/create.html'
    model = TrackerTeam
    form_class = TrackerTeamForm
    permissions = ['apptracker.create_trackerteam']

    def get_success_url(self):
        return reverse('team-list')


class TeamDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = TrackerTeam
    template_name = 'apptracker/projects/teams/confirm_delete.html'
    context_object_name = 'team'
    pk_url_kwarg = 'team_pk'
    permissions = ['apptracker.delete_trackerteam']

    def get_success_url(self):
        return reverse('team-list')


class TeamEditView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = TrackerTeam
    template_name = 'apptracker/projects/teams/edit.html'
    pk_url_kwarg = 'team_pk'
    form_class = TrackerTeamForm
    context_object_name = 'team'
    permissions = ['apptracker.edit_trackerteam']

    def get_success_url(self):
        return reverse('team-list')