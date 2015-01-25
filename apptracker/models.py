# -*- coding: utf-8 -*-

from django.db import models


class Project(models.Model):

    name = models.CharField('Name', max_length=80)
    description = models.CharField('Description', max_length=200)
    total_issue = models.IntegerField(default=0, null=False, blank=False)

    def __str__(self):
        return self.name


class Issue(models.Model):

    title = models.CharField('Title', max_length=140)
    # reference = models.IntegerField(default=0, null=False, blank=False)
    project = models.ForeignKey(Project, related_name='issues', null=False, blank=False)

    # class Meta:
    #    unique_together = ('reference', 'project')

    def __str__(self):
        return self.title