# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apptracker', '0002_issue_pull_request'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='description',
            field=models.TextField(verbose_name='Description', blank=True, default=''),
            preserve_default=True,
        ),
    ]
