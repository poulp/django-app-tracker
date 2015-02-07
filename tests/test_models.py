#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
test_django-app-tracker
------------

Tests for `django-app-tracker` models module.
"""

from django.test import TestCase
from django.utils.text import slugify
from django.contrib.auth.models import User

from apptracker.models import Project, Issue, IssueActivity, Label


class ProjectModelTest(TestCase):

    def setUp(self):
        self.project = Project.objects.create(
            name="Test name",
           description="Test description"
        )
        self.project.save()

    def test_str(self):
        self.assertEqual(self.project.name, self.project.__str__())


class LabelModelTest(TestCase):

    def setUp(self):
        self.project = Project.objects.create(
            name="Title",
            description="Description"
        )
        self.project.save()

        self.label1 = Label.objects.create(
            title="django python",
            color="#FFFFFF",
            project=self.project

        )
        self.label1.save()

    def test_str(self):
        self.assertEqual(
            self.label1.title,
            self.label1.__str__()
        )

    def test_save(self):
        self.assertEqual(self.label1.slug, slugify(self.label1.title))

class IssueModelTest(TestCase):

    def setUp(self):
        self.project1 = Project()
        self.project1.name = "project1"
        self.project1.description = "project1 description"
        self.project1.save()

        self.user = User.objects.create(
            username='poulp'
        )
        self.user.save()

        self.issue1 = Issue.objects.create(
            title="issue1",
            description="description",
            project=self.project1,
            owner=self.user
        )
        self.issue1.save()

    def test_str(self):
        self.assertEqual(self.issue1.title, self.issue1.__str__())

    def test_modified_date(self):
        self.issue1.title = "update title"
        self.issue1.save()
        self.assertNotEqual(self.issue1.created_date, self.issue1.modified_date)

    def test_markdown_to_html_in_save(self):
        self.assertEqual(
            "<p>description</p>",
            self.issue1.description_html
        )

    #def test_issue_activity(self):
    #    self.assertEqual(0, len(IssueActivity.objects.all()))

    #    self.issue1.title = "update title"
    #    self.issue1.save(update_fields=['title'])

    #    self.assertEqual(1, len(IssueActivity.objects.all()))
    #    issue_activity = IssueActivity.objects.get(pk=1)
    #    self.assertEqual(issue_activity.issue, self.issue1)
    #    self.assertEqual(issue_activity.attribute_changed, "title")
    #    self.assertEqual(issue_activity.__unicode__(), self.issue1.title+" "+issue_activity.attribute_changed)
