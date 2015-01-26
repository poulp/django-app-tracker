
from rest_framework import serializers

from .models import Project, Issue


class IssueItemSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Issue
        fields = ('pk', 'title')


class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = ('pk', 'name', 'description')


class ProjectIssuesListSerializer(serializers.HyperlinkedModelSerializer):
    issues = IssueItemSerializer(many=True)

    class Meta:
        model = Project
        fields = ('pk', 'name', 'issues')


class IssueDetailSerializer(serializers.HyperlinkedModelSerializer):
    project = ProjectSerializer(read_only=True)

    class Meta:
        model = Issue
        fields = ('pk', 'title', 'description', 'project', 'created_date', 'modified_date')
        read_only_fields = ('created_date', 'modified_date')

    def update(self, instance, validated_data):

        update_fields = []
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
            update_fields.append(attr)
        instance.save(update_fields = update_fields)

        return instance