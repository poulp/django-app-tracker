#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from django.test import TestCase
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User, Permission

from apptracker.models import TrackerTeam
from apptracker.settings import tracker_settings


class TeamListViewTest(TestCase):

    def setUp(self):
        # can't create a project
        self.user = User.objects.create_user(username='user', password='user')
        # can create a project
        self.manager = User.objects.create_user(username='manager', password='manager')

        # permission to create a project
        permission = Permission.objects.get(codename='view_trackerteam')

        self.manager.user_permissions.add(permission)

    def test_fail_access_member(self):
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