
from rest_framework import serializers

from .models import Project, Issue, IssueActivity


class IssueItemSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Issue
        fields = ('pk', 'title', 'reference')


class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = ('pk', 'name', 'description')


class ProjectIssuesListSerializer(serializers.HyperlinkedModelSerializer):
    issues = IssueItemSerializer(many=True)

    class Meta:
        model = Project
        fields = ('pk', 'name', 'issues')


class IssueActivitySerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = IssueActivity
        fields = ('pk', 'created_date', 'attribute_changed')


class IssueDetailSerializer(serializers.HyperlinkedModelSerializer):
    project = ProjectSerializer(read_only=True)
    activity = IssueActivitySerializer(read_only=True, many=True)

    class Meta:
        model = Issue
        fields = (
            'pk',
            'title',
            'description',
            'created_date',
            'modified_date',
            'project',
            'is_closed',
            'activity')
        read_only_fields = ('created_date', 'modified_date', 'reference')

    def update(self, instance, validated_data):

        update_fields = []
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
            update_fields.append(attr)
        instance.save(update_fields = update_fields)

        return instance