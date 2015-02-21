#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from django.views.generic.edit import FormView, DeleteView, UpdateView
from django.core.urlresolvers import reverse

from apptracker.mixins import ProjectMixin, AjaxableResponseMixin, LoginRequiredMixin, PermissionRequiredMixin
from apptracker.forms import LabelForm
from apptracker.models import Label


class ProjectLabelsView(PermissionRequiredMixin, LoginRequiredMixin, ProjectMixin, FormView):
    template_name = 'apptracker/projects/labels/list.html'
    form_class = LabelForm
    permissions = ['apptracker.view_label', 'apptracker.create_label']

    def get_success_url(self):
        return reverse('project-labels', kwargs={'project_pk': self.kwargs['project_pk']})

    def get_context_data(self, **kwargs):
        context = super(ProjectLabelsView, self).get_context_data(**kwargs)
        context['labels'] = self.get_project().labels.all
        return context

    def form_valid(self, form):
        label = form.save(commit=False)
        label.project = self.get_project()
        label.save()
        return super(ProjectLabelsView, self).form_valid(form)


class LabelEditView(LoginRequiredMixin, PermissionRequiredMixin, ProjectMixin, UpdateView):
    model = Label
    template_name = 'apptracker/projects/labels/edit.html'
    form_class = LabelForm
    context_object_name = 'label'
    pk_url_kwarg = 'label_pk'
    permissions = ['apptracker.edit_label']

    def get_success_url(self):
        return reverse('project-labels', kwargs={'project_pk': self.kwargs['project_pk']})


class LabelDeleteView(LoginRequiredMixin, PermissionRequiredMixin, AjaxableResponseMixin, DeleteView):
    model = Label
    pk_url_kwarg = 'label_pk'
    template_name = 'apptracker/projects/labels/confirm_delete.html'
    permissions = ['apptracker.delete_label']

    def get_success_url(self):
        return reverse('project-list')