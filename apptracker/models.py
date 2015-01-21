# -*- coding: utf-8 -*-

from django.db import models

class Project(models.Model):

    name = models.CharField('Name', max_length=80)