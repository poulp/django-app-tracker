# -*- coding: utf-8 -*-

from django.db import models
from django.dispatch import receiver
from django.utils import timezone
from django.db.models.signals import pre_save, post_save


class Project(models.Model):

    name = models.CharField('Name', max_length=80)
    description = models.CharField('Description', max_length=200)
    total_issue = models.IntegerField(default=0, null=False, blank=False)

    def __str__(self):
        return self.name


class Issue(models.Model):

    title = models.CharField('Title', max_length=140)
    description = models.TextField('Description', null=False, blank=False)
    reference = models.IntegerField(default=0, null=False, blank=False)
    project = models.ForeignKey(Project, related_name='issues', null=False, blank=False)

    created_date = models.DateTimeField('Created date', null=False, blank=False, default=timezone.now)
    modified_date = models.DateTimeField('Modified date', null=False, blank=False, default=timezone.now)

    class Meta:
        unique_together = ('reference', 'project')

    def __str__(self):
        return self.title


class IssueActivity(models.Model):
    issue = models.ForeignKey(Issue, related_name="activity", null=False, blank=False)
    attribute_changed = models.CharField('Changed', max_length=200)
    created_date = models.DateTimeField('Created date', null=False, blank=False, default=timezone.now)


@receiver(pre_save, sender=Issue)
def pre_save_issue(sender, instance, **kwargs):
    instance.modified_date = timezone.now()
    instance.reference = instance.project.total_issue + 1


@receiver(post_save, sender=Issue)
def post_save_issue(sender, instance, **kwargs):
    updated_fields = kwargs.get('update_fields', [])
    created = kwargs.get('created', True)

    if not created and updated_fields:
        for field in updated_fields:
            issue_activity = IssueActivity()
            issue_activity.issue = instance
            issue_activity.attribute_changed = field
            issue_activity.save()

    # update total issues for the project
    project = instance.project
    project.total_issue = project.total_issue + 1
    project.save()