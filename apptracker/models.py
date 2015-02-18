#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from django.db import models
from django.utils import timezone
from django.utils.safestring import mark_safe
from django.utils.encoding import smart_text
from django.utils.text import slugify
from django.contrib.auth.models import User, Group

from markdown import markdown


class Project(models.Model):

    class Meta(object):
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'
        ordering = ['slug']
        default_permissions = ('create', 'edit', 'delete', 'view')

    name = models.CharField('Name', max_length=80)
    slug = models.CharField('Slug', max_length=80)
    description = models.CharField('Description', max_length=200)

    repository = models.URLField('Repository', blank=True)
    documentation = models.URLField('Documentation', blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Label(models.Model):

    class Meta(object):
        verbose_name = 'Label'
        verbose_name_plural = 'Labels'
        ordering = ['color']
        default_permissions = ('create', 'edit', 'delete', 'view')


    title = models.CharField(max_length=20, verbose_name='Title')
    slug = models.SlugField(max_length=20, verbose_name='Slug')
    color = models.CharField(max_length=7, default="#2D3E63", verbose_name='Color')
    project = models.ForeignKey(Project, related_name='labels', null=False, blank=False)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.title = smart_text(self.title).lower()
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class Issue(models.Model):

    class Meta(object):
        verbose_name = 'Issue'
        verbose_name_plural = 'Issues'
        ordering = ['-pk']
        default_permissions = ('create', 'edit', 'delete', 'view')


    title = models.CharField('Title', max_length=140)
    description = models.TextField('Description', default='', blank=True)
    description_html = models.TextField('Description Html')
    owner = models.ForeignKey(User, null=False, blank=False, related_name='owned_issues')

    project = models.ForeignKey(Project, related_name='issues', null=False, blank=False)
    labels = models.ManyToManyField(Label, related_name='issues', blank=True)

    is_closed = models.BooleanField(default=False, null=False, blank=False)
    pull_request = models.URLField(default='', blank=True)

    created_date = models.DateTimeField('Created date', null=False, blank=False, default=timezone.now)
    modified_date = models.DateTimeField('Modified date', null=False, blank=False, default=timezone.now)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.modified_date = timezone.now()

        if self.description:
            self.description_html = mark_safe(markdown(self.description))

        super().save(*args, **kwargs)


class Comment(models.Model):

    class Meta(object):
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
        ordering = ['pk']
        default_permissions = ('create', 'edit', 'view')


    author = models.ForeignKey(User, related_name='user_comments')
    is_issue_owner = models.BooleanField(default=False)
    issue = models.ForeignKey(Issue, related_name='comments')
    text = models.TextField('Text')
    text_html = models.TextField('Text Html')

    created_date = models.DateTimeField('Created date', default=timezone.now)
    modified_date = models.DateTimeField('Modified date', default=timezone.now)

    def save(self, *args, **kwargs):
        self.modified_date = timezone.now()

        if self.text:
            self.text_html = mark_safe(markdown(self.text))

        super().save(*args, **kwargs)

        #@receiver(post_save, sender=Issue)
        #def post_save_issue(sender, instance, **kwargs):
        # updated_fields = kwargs.get('update_fields', [])

        # if not created and updated_fields:
        #    for field in updated_fields:
        #        issue_activity = IssueActivity()
        #        issue_activity.issue = instance
        #        issue_activity.attribute_changed = field
        #        issue_activity.save()


class IssueActivity(models.Model):

    class Meta(object):
        verbose_name = 'Issue Activity'
        verbose_name_plural = 'Issue Activities'

    issue = models.ForeignKey(Issue, related_name="activity", null=False, blank=False)
    attribute_changed = models.CharField('Changed', max_length=200)
    created_date = models.DateTimeField('Created date', null=False, blank=False, default=timezone.now)

    def __str__(self):
        return self.issue.title + " " + self.attribute_changed


class TrackerTeam(Group):

    class Meta(object):
        verbose_name = 'Team'
        verbose_name_plural = 'Teams'
        default_permissions = ('create', 'edit', 'delete', 'view')

    color = models.CharField(max_length=7, default="#2D3E63", verbose_name='Color')