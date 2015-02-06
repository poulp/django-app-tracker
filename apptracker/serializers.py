
from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Project, Issue, IssueActivity, Label


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta(object):
        model = User
        fields = ('username',)


class LabelSerializer(serializers.HyperlinkedModelSerializer):

    class Meta(object):
        model = Label
        fields = ('pk', 'title', 'color')


class IssueItemSerializer(serializers.HyperlinkedModelSerializer):
    labels = LabelSerializer(many=True, required=False)
    owner = UserSerializer(read_only=True)

    class Meta(object):
        model = Issue
        fields = ('pk', 'title', 'reference', 'created_date', 'labels', 'owner')


class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    labels = LabelSerializer(many=True, read_only=True)

    class Meta(object):
        model = Project
        fields = ('pk', 'name', 'description', 'labels')


class ProjectIssuesListSerializer(serializers.HyperlinkedModelSerializer):
    issues = IssueItemSerializer(many=True)

    class Meta(object):
        model = Project
        fields = ('pk', 'name', 'issues')


class IssueActivitySerializer(serializers.HyperlinkedModelSerializer):

    class Meta(object):
        model = IssueActivity
        fields = ('pk', 'created_date', 'attribute_changed')


class IssueDetailSerializer(serializers.HyperlinkedModelSerializer):
    project = ProjectSerializer(read_only=True)
    activity = IssueActivitySerializer(read_only=True, many=True)
    labels = LabelSerializer(many=True, required=False)
    owner = UserSerializer(read_only=True)

    class Meta(object):
        model = Issue
        fields = (
            'pk',
            'title',
            'description',
            'created_date',
            'modified_date',
            'project',
            'is_closed',
            'activity',
            'description_html',
            'labels',
            'owner'
        )
        read_only_fields = ('created_date', 'modified_date', 'reference', 'description_html')

    #def update(self, instance, validated_data):
    #    update_fields = []
    #    for attr, value in validated_data.items():
    #        setattr(instance, attr, value)
    #        update_fields.append(attr)
    #    instance.save(validated_data = update_fields)
    #    return instance