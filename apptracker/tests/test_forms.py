
from django.test import TestCase

from apptracker.models import Project, Label
from apptracker.forms import NewIssueForm, IssueFilterForm

class NewIssueFormTest(TestCase):

    def setUp(self):
        self.project = Project.objects.create(
            name='project'
        )

        self.project2 = Project.objects.create(
            name='project2'
        )

        Label.objects.create(
            title='label1',
            color='#FFFFFF',
            project=self.project
        )

        Label.objects.create(
            title='label2',
            color='#FFFFFF',
            project=self.project2
        )

    def test_labels_belong_to_project(self):
        form = NewIssueForm(self.project)
        self.assertEqual(1, len(form.fields['labels'].queryset))
        self.assertEqual(self.project, form.fields['labels'].queryset[0].project)


class IssueFilterFormTest(TestCase):

    def setUp(self):
        self.project = Project.objects.create(
            name='project'
        )

        self.project2 = Project.objects.create(
            name='project2'
        )

        Label.objects.create(
            title='label1',
            color='#FFFFFF',
            project=self.project
        )

        Label.objects.create(
            title='label2',
            color='#FFFFFF',
            project=self.project2
        )

    def test_labels_belong_to_project(self):
        form = IssueFilterForm(self.project)
        self.assertEqual(1, len(form.fields['labels'].queryset))
        self.assertEqual(self.project, form.fields['labels'].queryset[0].project)