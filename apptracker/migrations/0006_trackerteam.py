# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
        ('apptracker', '0005_auto_20150215_0654'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrackerTeam',
            fields=[
                ('group_ptr', models.OneToOneField(primary_key=True, serialize=False, to='auth.Group', parent_link=True, auto_created=True)),
                ('color', models.CharField(max_length=7, default='#2D3E63', verbose_name='Color')),
            ],
            options={
                'verbose_name_plural': 'Teams',
                'verbose_name': 'Team',
            },
            bases=('auth.group',),
        ),
    ]
