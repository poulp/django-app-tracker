from django.http import HttpResponse
from rest_framework import viewsets
from django.shortcuts import render

from .models import Project
from .serializers import ProjectSerializer


def index(request):
    return render(request, "apptracker/base.html", {})


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer