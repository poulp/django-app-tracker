#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
test_django-app-tracker
------------

Tests for `django-app-tracker` serializers module.
"""

from django.test import TestCase

from apptracker.serializers import UserSerializer, LabelSerializer


class UserSerializerTest(TestCase):

    def setUp(self):
        self.user_data = {
            'username': 'poulp'
        }

    def test_valid_user(self):
        serializer = UserSerializer(data=self.user_data)
        self.assertTrue(serializer.is_valid())


class LabelSerializerTest(TestCase):

    def setUp(self):
        self.label_data = {
            'title': 'python',
            'color': '#FFFFFF',
            'slug': 'python'
        }

    def test_valid_label(self):
        serializer = LabelSerializer(data=self.label_data)
        self.assertTrue(serializer.is_valid())

    def test_invalid_color(self):

        # max size test
        self.label_data['color'] = '#FFFFFFX'
        serializer = LabelSerializer(data=self.label_data)
        self.assertFalse(serializer.is_valid())

        # strip
        self.label_data['color'] = ' '
        serializer = LabelSerializer(data=self.label_data)
        self.assertFalse(serializer.is_valid())

    def test_invalid_title(self):

        # empty
        self.label_data['title'] = ''
        serializer = LabelSerializer(data=self.label_data)
        self.assertFalse(serializer.is_valid())

        # strip
        self.label_data['title'] = ' '
        serializer = LabelSerializer(data=self.label_data)
        self.assertFalse(serializer.is_valid())