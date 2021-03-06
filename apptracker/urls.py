#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from django.conf.urls import include, url

from apptracker.views import projects, issues, teams, labels


project_urls = [
    # Projects
    url(r'^$', projects.ProjectListView.as_view(), name='project-list'),
    url(r'^create/$', projects.ProjectCreateView.as_view(), name='project-create'),
    url(r'^(?P<project_pk>[0-9]+)/edit$', projects.ProjectUpdateView.as_view(), name='project-edit'),
    url(r'^(?P<project_pk>[0-9]+)/delete$', projects.ProjectDeleteView.as_view(), name='project-delete'),

    # Groups and permissions
    url(r'^team$', teams.TeamListView.as_view(), name='team-list'),
    url(r'^team/create$', teams.TeamCreateView.as_view(), name='team-create'),
    url(r'^team/(?P<team_pk>[0-9]+)/edit', teams.TeamEditView.as_view(), name='team-edit'),
    url(r'^team/(?P<team_pk>[0-9]+)/delete', teams.TeamDeleteView.as_view(), name='team-delete'),

    # Labels
    url(r'^(?P<project_pk>[0-9]+)/labels/$', labels.ProjectLabelsView.as_view(), name='project-labels'),
    url(r'^(?P<project_pk>[0-9]+)/labels/(?P<label_pk>[0-9]+)/edit', labels.LabelEditView.as_view(), name='label-edit'),
    url(r'^(?P<project_pk>[0-9]+)/labels/(?P<label_pk>[0-9]+)/delete$', labels.LabelDeleteView.as_view(), name='label-delete'),

    # Issues
    url(r'^(?P<project_pk>[0-9]+)/issues/$', issues.IssuesListView.as_view(), name='issue-list'),
    url(r'^(?P<project_pk>[0-9]+)/issues/(?P<issue_pk>[0-9]+)$', issues.IssueDetailView.as_view(), name='issue-detail'),
    url(r'^(?P<project_pk>[0-9]+)/issues/(?P<issue_pk>[0-9]+)/edit$', issues.IssueEditView.as_view(), name='issue-edit'),
    url(r'^(?P<project_pk>[0-9]+)/issues/(?P<issue_pk>[0-9]+)/close', issues.IssueCloseView.as_view(), name='issue-close'),
    url(r'^(?P<project_pk>[0-9]+)/issues/(?P<issue_pk>[0-9]+)/comment', issues.IssueCommentView.as_view(), name='issue-comment'),
    url(r'^(?P<project_pk>[0-9]+)/issue/new/$', issues.IssueCreateView.as_view(), name='issue-new'),
    url(r'^(?P<project_pk>[0-9]+)/issues/(?P<issue_pk>[0-9]+)/delete$', issues.IssueDeleteView.as_view(), name='issue-delete'),
]

urlpatterns = [
    url(r'^projects/', include(project_urls)),
]