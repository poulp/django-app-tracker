
from rest_framework import serializers

from .models import Project, Issue


class IssueSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Issue
        fields = ('pk', 'title')


class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = ('pk', 'name', 'description')


class ProjectIssuesSerializer(serializers.HyperlinkedModelSerializer):
    issues = IssueSerializer(many=True)

    class Meta:
        model = Project
        fields = ('pk', 'name', 'issues')