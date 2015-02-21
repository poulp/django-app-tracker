#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from django.test import TestCase
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User, Permission

from apptracker.models import Project


class ProjectListViewTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='user', password='user')

    def test_access_anonymous(self):
        response = self.client.get(reverse('project-list'))
        self.assertEqual(200, response.status_code)

    def test_access_member(self):
        self.assertTrue(
            self.client.login(
                username='user',
                password='user'
            )
        )

        response = self.client.get(reverse('project-list'))
        self.assertEqual(200, response.status_code)

    def test_get_project_list(self):
        Project.objects.create(name='test')
        Project.objects.create(name='test2')

        response = self.client.get(reverse('project-list'))
        self.assertEqual(200, response.status_code)
        self.assertEqual(2, len(response.context['projects']))


class ProjectCreateViewTest(TestCase):

    def setUp(self):
        # can't create a project
        self.user = User.objects.create_user(username='user', password='user')
        # can create a project
        self.manager = User.objects.create_user(username='manager', password='manager')

        # permission to create a project
        permission = Permission.objects.get(codename='create_project')
        self.manager.user_permissions.add(permission)

    def test_denies_anonymous(self):

        response = self.client.get(reverse('project-create'))
        self.assertEqual(403, response.status_code)

        response = self.client.post(reverse('project-create'), {
            'name': 'test project',
            'description': 'test description'
        })

        self.assertEqual(403, response.status_code)
        self.assertEqual(0, len(Project.objects.all()))

    def test_can_create_project(self):
        self.assertEqual(0, len(Project.objects.all()))

        self.assertTrue(
            self.client.login(
                username='manager',
                password='manager'
            )
        )

        response = self.client.get(reverse('project-create'))
        self.assertEqual(200, response.status_code)

        response = self.client.post(reverse('project-create'), {
            'name': 'test project',
            'description': 'test description'
        }, follow=True)

        self.assertEqual(200, response.status_code)
        self.assertEqual(1, len(Project.objects.all()))

    def test_cant_create_project(self):
        self.assertEqual(0, len(Project.objects.all()))

        self.assertTrue(
            self.client.login(
                username='user',
                password='user'
            )
        )

        response = self.client.get(reverse('project-create'))
        self.assertEqual(403, response.status_code)

        response = self.client.post(reverse('project-create'), {
            'name': 'test project',
            'description': 'test description'
        })

        self.assertEqual(403, response.status_code)
        self.assertEqual(0, len(Project.objects.all()))


class ProjectEditViewTest(TestCase):

    def setUp(self):
        # can't edit a project
        self.user = User.objects.create_user(username='user', password='user')
        # can edit a project
        self.manager = User.objects.create_user(username='manager', password='manager')

        # permission to edit a project
        permission = Permission.objects.get(codename='edit_project')
        self.manager.user_permissions.add(permission)

        self.project = Project.objects.create(
            name='test',
            description='test'
        )

    def test_denies_anonymous(self):

        response = self.client.get(reverse('project-edit', kwargs={'project_pk': self.project.pk}))
        self.assertEqual(403, response.status_code)

        response = self.client.post(reverse('project-edit', kwargs={'project_pk': self.project.pk}), {
            'name': 'edit name',
            'description': 'edit description'
        })

        self.assertEqual(403, response.status_code)
        self.assertNotEqual('edit name', Project.objects.get(pk=1).name)
        self.assertNotEqual('edit description', Project.objects.get(pk=1).description)

    def test_can_edit_project(self):

        self.assertTrue(
            self.client.login(
                username='manager',
                password='manager'
            )
        )

        response = self.client.get(reverse('project-edit', kwargs={'project_pk': self.project.pk}))
        self.assertEqual(200, response.status_code)

        response = self.client.post(reverse('project-edit', kwargs={'project_pk': self.project.pk}), {
            'name': 'edit name',
            'description': 'edit description'
        }, follow=True)

        self.assertEqual(200, response.status_code)
        self.assertEqual('edit name', Project.objects.get(pk=1).name)
        self.assertEqual('edit description', Project.objects.get(pk=1).description)

    def test_cant_create_project(self):
        self.assertTrue(
            self.client.login(
                username='user',
                password='user'
            )
        )

        response = self.client.get(reverse('project-edit', kwargs={'project_pk': self.project.pk}))
        self.assertEqual(403, response.status_code)

        response = self.client.post(reverse('project-edit', kwargs={'project_pk': self.project.pk}), {
            'name': 'edit name',
            'description': 'edit description'
        })

        self.assertEqual(403, response.status_code)
        self.assertNotEqual('edit name', Project.objects.get(pk=1).name)
        self.assertNotEqual('edit description', Project.objects.get(pk=1).description)


class ProjectDeleteViewTest(TestCase):

    def setUp(self):
        # can't create a project
        self.user = User.objects.create_user(username='user', password='user')
        # can create a project
        self.manager = User.objects.create_user(username='manager', password='manager')

        # permission to create a project
        permission = Permission.objects.get(codename='delete_project')
        self.manager.user_permissions.add(permission)

        self.project = Project.objects.create(
            name='test',
            description='test'
        )

    def test_denies_anonymous(self):
        response = self.client.get(reverse('project-delete', kwargs={'project_pk': self.project.pk}))
        self.assertEqual(403, response.status_code)

        response = self.client.post(reverse('project-delete', kwargs={'project_pk': self.project.pk}))

        self.assertEqual(403, response.status_code)
        self.assertEqual(1, len(Project.objects.all()))

    def test_can_delete_project(self):
        self.assertTrue(
            self.client.login(
                username='manager',
                password='manager'
            )
        )

        response = self.client.get(reverse('project-delete', kwargs={'project_pk': self.project.pk}))
        self.assertEqual(200, response.status_code)

        response = self.client.post(reverse('project-delete', kwargs={'project_pk': self.project.pk}), follow=True)

        self.assertEqual(200, response.status_code)
        self.assertEqual(0, len(Project.objects.all()))

    def test_cant_delete_project(self):
        self.assertTrue(
            self.client.login(
                username='user',
                password='user'
            )
        )

        response = self.client.get(reverse('project-delete', kwargs={'project_pk': self.project.pk}))
        self.assertEqual(403, response.status_code)

        response = self.client.post(reverse('project-delete', kwargs={'project_pk': self.project.pk}))

        self.assertEqual(403, response.status_code)
        self.assertEqual(1, len(Project.objects.all()))