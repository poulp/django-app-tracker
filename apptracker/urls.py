from django.conf.urls import include, url

from .routers import router

urlpatterns = [
    url(r'^api/', include(router.urls)),
    url(r'^tracker-api/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^angular/', 'apptracker.views.index')
]
