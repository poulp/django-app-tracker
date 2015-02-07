
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from rest_framework import serializers

from .models import Project, Issue, IssueActivity, Label


class UserSerializer(serializers.ModelSerializer):

    class Meta(object):
        model = User
        fields = ('username',)


class LabelSerializer(serializers.ModelSerializer):

    class Meta(object):
        model = Label
        fields = ('pk', 'title', 'slug', 'color')
        read_only_fields = ('slug')


class IssueItemSerializer(serializers.ModelSerializer):
    labels = LabelSerializer(many=True, required=False)
    owner = UserSerializer(read_only=True)

    class Meta(object):
        model = Issue
        fields = ('pk', 'title', 'reference', 'created_date', 'labels', 'owner')


class ProjectSerializer(serializers.ModelSerializer):
    labels = LabelSerializer(many=True, read_only=True)

    class Meta(object):
        model = Project
        fields = ('pk', 'name', 'description', 'labels')


class ProjectIssuesListSerializer(serializers.ModelSerializer):
    issues = IssueItemSerializer(many=True)

    class Meta(object):
        model = Project
        fields = ('pk', 'name', 'issues')


class IssueActivitySerializer(serializers.ModelSerializer):

    class Meta(object):
        model = IssueActivity
        fields = ('pk', 'created_date', 'attribute_changed')


class IssueDetailSerializer(serializers.ModelSerializer):
    project = ProjectSerializer(read_only=True)
    #activity = IssueActivitySerializer(read_only=True, many=True)
    labels = LabelSerializer(many=True, required=False)
    owner = UserSerializer(read_only=True)

    class Meta(object):
        model = Issue
        fields = (
            'pk',
            'title',
            'description',
            'reference',
            'project',
            'created_date',
            'modified_date',
            'is_closed',
            'description_html',
            'owner',
            'labels',
            'reference'
        )
        read_only_fields = (
            'created_date',
            'modified_date',
            'reference',
            'description_html',
        )
        validators = []

    def create(self, validated_data):

        issue = Issue.objects.create(
            title = validated_data['title'],
            description = validated_data['description'],
            owner = validated_data['owner'],
            project = validated_data['project'],
            reference = validated_data['reference']
        )

        if 'labels' in validated_data:
            for label in validated_data['labels']:
                label = get_object_or_404(Label, slug=label['slug'], project=validated_data['project'])
                issue.labels.add(label)

        return issue

    #def update(self, instance, validated_data):
    #    update_fields = []
    #    for attr, value in validated_data.items():
    #        setattr(instance, attr, value)
    #        update_fields.append(attr)
    #    instance.save(validated_data = update_fields)
    #    return instance