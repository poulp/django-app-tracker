#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from django.test import TestCase
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User, Permission, Group

from apptracker.models import TrackerTeam
from apptracker.settings import tracker_settings


class TeamListViewTest(TestCase):

    def setUp(self):
        # can't create a project
        self.user = User.objects.create_user(username='user', password='user')
        # can create a project
        self.manager = User.objects.create_user(username='manager', password='manager')

        # permission to view a team
        permission = Permission.objects.get(codename='view_trackerteam')

        self.manager.user_permissions.add(permission)

    def test_fail_access_permission(self):
        self.assertTrue(
            self.client.login(
                username='user',
                password='user'
            )
        )

        response = self.client.get(reverse('team-list'), follow=False)
        self.assertEqual(403, response.status_code)

    def test_get_project_list(self):
        TrackerTeam.objects.create(name='test')
        TrackerTeam.objects.create(name='test2')

        self.assertTrue(
            self.client.login(
                username='manager',
                password='manager'
            )
        )

        response = self.client.get(reverse('team-list'))
        self.assertEqual(200, response.status_code)
        self.assertEqual(2, len(response.context['teams']))


class TeamCreateViewTest(TestCase):

    def setUp(self):
        # can't create a project
        self.user = User.objects.create_user(username='user', password='user')
        # can create a project
        self.manager = User.objects.create_user(username='manager', password='manager')

        # permission to view a team
        self.permission_create = Permission.objects.get(codename='create_trackerteam')
        self.permission_view = Permission.objects.get(codename='view_trackerteam')

        self.manager.user_permissions.add(self.permission_create)
        self.manager.user_permissions.add(self.permission_view)

    def test_fail_create_permission(self):
        self.assertTrue(
            self.client.login(
                username='user',
                password='user'
            )
        )

        response = self.client.get(reverse('team-create'), follow=False)
        self.assertEqual(403, response.status_code)

        response = self.client.post(reverse('team-create'), {
            'name': 'test',
            'color': '#FFFFFF',
            'permissions': ()
        })
        self.assertEqual(403, response.status_code)
        self.assertEqual(0, len(TrackerTeam.objects.all()))

    def test_create_team(self):
        self.assertTrue(
            self.client.login(
                username='manager',
                password='manager'
            )
        )

        response = self.client.get(reverse('team-create'), follow=False)
        self.assertEqual(200, response.status_code)

        response = self.client.post(reverse('team-create'), {
            'name': 'test',
            'color': '#FFFFFF',
            'permissions': (self.permission_create.pk, self.permission_view.pk)
        }, follow=True)
        self.assertEqual(200, response.status_code)
        self.assertEqual(1, len(TrackerTeam.objects.all()))


class TeamDeleteViewTest(TestCase):
    def setUp(self):
        # can't create a project
        self.user = User.objects.create_user(username='user', password='user')
        # can create a project
        self.manager = User.objects.create_user(username='manager', password='manager')

        # permission to view a team
        self.permission_delete = Permission.objects.get(codename='delete_trackerteam')
        self.permission_view = Permission.objects.get(codename='view_trackerteam')

        self.manager.user_permissions.add(self.permission_delete)
        self.manager.user_permissions.add(self.permission_view)

        TrackerTeam.objects.create(
            name='test',
            color='#FFFFFF'
        )

    def test_fail_delete_permission(self):
        self.assertTrue(
            self.client.login(
                username='user',
                password='user'
            )
        )

        response = self.client.get(reverse('team-delete', kwargs={'team_pk': 1}), follow=False)
        self.assertEqual(403, response.status_code)

        response = self.client.post(reverse('team-delete', kwargs={'team_pk': 1}))
        self.assertEqual(403, response.status_code)
        self.assertEqual(1, len(TrackerTeam.objects.all()))

    def test_delete_team(self):
        self.assertTrue(
            self.client.login(
                username='manager',
                password='manager'
            )
        )

        response = self.client.get(reverse('team-delete', kwargs={'team_pk': 1}), follow=False)
        self.assertEqual(200, response.status_code)

        response = self.client.post(reverse('team-delete', kwargs={'team_pk': 1}), follow=True)
        self.assertEqual(200, response.status_code)
        self.assertEqual(0, len(TrackerTeam.objects.all()))


class TeamEditViewTest(TestCase):
    def setUp(self):
        # can't create a project
        self.user = User.objects.create_user(username='user', password='user')
        # can create a project
        self.manager = User.objects.create_user(username='manager', password='manager')

        # permission to view a team
        self.permission_edit = Permission.objects.get(codename='edit_trackerteam')
        self.permission_view = Permission.objects.get(codename='view_trackerteam')

        self.manager.user_permissions.add(self.permission_edit)
        self.manager.user_permissions.add(self.permission_view)

        TrackerTeam.objects.create(
            name='test',
            color='#FFFFFF'
        )

    def test_fail_edit_permission(self):
        self.assertTrue(
            self.client.login(
                username='user',
                password='user'
            )
        )

        response = self.client.get(reverse('team-edit', kwargs={'team_pk': 1}))
        self.assertEqual(403, response.status_code)

        response = self.client.post(reverse('team-edit', kwargs={'team_pk': 1}), {
            'name': 'edit',
            'color': '#000000'
        })
        self.assertEqual(403, response.status_code)
        self.assertEqual(1, len(TrackerTeam.objects.all()))
        team = TrackerTeam.objects.get(pk=1)
        self.assertEqual('test', team.name)

    def test_edit_team(self):
        self.assertTrue(
            self.client.login(
                username='manager',
                password='manager'
            )
        )

        response = self.client.get(reverse('team-edit', kwargs={'team_pk': 1}))
        self.assertEqual(200, response.status_code)

        response = self.client.post(reverse('team-edit', kwargs={'team_pk': 1}), {
            'name': 'edit',
            'color': '#000000'
        }, follow=True)

        self.assertEqual(200, response.status_code)
        self.assertEqual(1, len(TrackerTeam.objects.all()))
        team = TrackerTeam.objects.get(pk=1)
        self.assertEqual('edit', team.name)
        self.assertEqual('#000000', team.color)