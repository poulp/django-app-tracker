# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apptracker', '0004_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'verbose_name_plural': 'Comments', 'verbose_name': 'Comment', 'ordering': ['pk']},
        ),
        migrations.AddField(
            model_name='comment',
            name='is_issue_owner',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
