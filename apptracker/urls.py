from django.conf.urls import include, url

from .api import ProjectList, ProjectIssues


project_urls =[
    url(r'^$', ProjectList.as_view(), name='project-list'),
    url(r'^/(?P<pk>[0-9]+)/issues$', ProjectIssues.as_view(), name='project-issues'),

]

urlpatterns = [
    url(r'^api/project', include(project_urls)),
    url(r'^angular/', 'apptracker.views.index')
]
