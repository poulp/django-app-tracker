#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_django-app-tracker
------------

Tests for `django-app-tracker` models module.
"""

from django.test import TestCase

from apptracker.models import Project, Issue, IssueActivity


class ProjectModelTest(TestCase):

    def setUp(self):
        self.project = Project()
        self.project.name = "Test name"
        self.project.description = "Test description"
        self.project.save()

    def test_total_issue(self):
        self.assertEqual(0, self.project.total_issue)

    def test_str(self):
        self.assertEqual(self.project.name, self.project.__str__())

    def test_unicode(self):
        self.assertEqual(self.project.name, self.project.__unicode__())


class IssueModelTest(TestCase):

    def setUp(self):
        self.project1 = Project()
        self.project1.title = "project1"
        self.project1.description = "project1 description"
        self.project1.save()

        self.issue1 = Issue()
        self.issue1.title = "issue1"
        self.issue1.description = "issue1 description"
        self.issue1.project = self.project1
        self.issue1.save()

    def test_str(self):
        self.assertEqual(self.issue1.title, self.issue1.__str__())

    def test_unicode(self):
        self.assertEqual(self.issue1.title, self.issue1.__unicode__())

    def test_issue_reference(self):
        self.assertEqual(0, self.issue1.reference)
        self.assertEqual(1, self.project1.total_issue)

        issue2 = Issue()
        issue2.title = "issue2"
        issue2.description = "issue2 description"
        issue2.project = self.project1
        issue2.save()

        self.assertEqual(0, self.issue1.reference)
        self.assertEqual(1, issue2.reference)
        self.assertEqual(2, self.project1.total_issue)

        self.issue1.delete()
        self.assertEqual(2, self.project1.total_issue)

    def test_modified_date(self):
        self.issue1.title = "update title"
        self.issue1.save()
        self.assertNotEqual(self.issue1.created_date, self.issue1.modified_date)

    def test_issue_activity(self):
        self.assertEqual(0, len(IssueActivity.objects.all()))

        self.issue1.title = "update title"
        self.issue1.save(update_fields=['title'])

        self.assertEqual(1, len(IssueActivity.objects.all()))
        issue_activity = IssueActivity.objects.get(pk=1)
        self.assertEqual(issue_activity.issue, self.issue1)
        self.assertEqual(issue_activity.attribute_changed, "title")
        self.assertEqual(issue_activity.__unicode__(), self.issue1.title+" "+issue_activity.attribute_changed)
