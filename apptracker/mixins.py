#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied

from apptracker.models import Project, Issue
from apptracker.settings import tracker_settings


class ProjectMixin(object):
    def get_project(self):
        return get_object_or_404(Project, pk=self.kwargs['project_pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['project'] = self.get_project()
        return context


class IssueMixin(object):
    def get_issue(self):
        return get_object_or_404(Issue, pk=self.kwargs['issue_pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['issue'] = self.get_issue()
        return context


class AjaxableResponseMixin(object):
    """
    Mixin to add AJAX support to a form.
    Must be used with an object-based FormView (e.g. CreateView)
    """
    def form_invalid(self, form):
        response = super().form_invalid(form)
        if self.request.is_ajax():
            return JsonResponse(form.errors, status=400)
        else:
            return response

    def form_valid(self, form):
        # We make sure to call the parent's form_valid() method because
        # it might do some processing (in the case of CreateView, it will
        # call form.save() for example).
        response = super().form_valid(form)
        if self.request.is_ajax():
            data = {
                'pk': self.object.pk,
            }
            return JsonResponse(data)
        else:
            return response


class LoginRequiredMixin(object):

    @method_decorator(login_required(login_url=tracker_settings.LOGIN_URL))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class PermissionRequiredMixin(object):
    permissions = []

    def dispatch(self, *args, **kwargs):
        if not self.request.user.has_perms(self.permissions):
            raise PermissionDenied
        return super().dispatch(*args, **kwargs)