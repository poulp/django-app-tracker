#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from rest_framework.serializers import ValidationError


def validator_strip(value):
    if value.strip() == "":
        raise ValidationError('This field must not be empty.')