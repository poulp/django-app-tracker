# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apptracker', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='issue',
            name='pull_request',
            field=models.URLField(blank=True, default=''),
            preserve_default=True,
        ),
    ]
