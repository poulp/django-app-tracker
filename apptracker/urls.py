#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from django.conf.urls import include, url

from apptracker.views import projects, issues


project_urls = [
    # Projects
    url(r'^$', projects.ProjectListView.as_view(), name='project-list'),
    url(r'^create/$', projects.ProjectCreateView.as_view(), name='project-create'),
    url(r'^(?P<pk>[0-9]+)/$', projects.ProjectDetailView.as_view(), name='project-detail'),
    url(r'^(?P<pk>[0-9]+)/edit$', projects.ProjectUpdateView.as_view(), name='project-edit'),


    # Labels
    url(r'^(?P<pk>[0-9]+)/labels/$', projects.ProjectLabelsView.as_view(), name='project-labels'),
    url(r'^(?P<pk>[0-9]+)/labels/(?P<label_pk>[0-9]+)/delete$', projects.LabelDeleteView.as_view(), name='label-delete'),

    # Issues
    url(r'^(?P<pk>[0-9]+)/issues/$', issues.IssuesListView.as_view(), name='issue-list'),
    url(r'^(?P<pk>[0-9]+)/issues/(?P<issue_pk>[0-9]+)$', issues.IssueDetailView.as_view(), name='issue-detail'),
    url(r'^(?P<pk>[0-9]+)/issues/(?P<issue_pk>[0-9]+)/edit$', issues.IssueEditView.as_view(), name='issue-edit'),
    url(r'^(?P<pk>[0-9]+)/issue/new/$', issues.IssueNewView.as_view(), name='issue-new'),
    url(r'^(?P<pk>[0-9]+)/issues/(?P<issue_pk>[0-9]+)/delete$', issues.IssueDeleteView.as_view(), name='issue-delete'),

]

urlpatterns = [
    url(r'^projects/', include(project_urls)),
    url(r'^$', 'apptracker.views.general.home', name='apptracker-home')
]
