from django.conf.urls import include, url

from .api import ProjectListView, ProjectIssuesListView, IssueDetailView, ProjectDetailView, ProjectLabelsView


project_urls =[
    url(r'^$', ProjectListView.as_view(), name='project-list'),
    url(r'^/(?P<pk>[0-9]+)$', ProjectDetailView.as_view(), name='project-detail'),
    url(r'^/(?P<project_pk>[0-9]+)/labels$', ProjectLabelsView.as_view(), name='project-labels'),
    url(r'^/(?P<pk>[0-9]+)/issues$', ProjectIssuesListView.as_view(), name='project-issues'),
    url(r'^/(?P<project_pk>[0-9]+)/issues/(?P<issue_reference>[0-9]+)$', IssueDetailView.as_view(), name='issue-detail'),
]

urlpatterns = [
    url(r'^api/project', include(project_urls)),
    url(r'^angular/', 'apptracker.views.index')
]
