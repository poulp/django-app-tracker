# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('apptracker', '0003_auto_20150213_1046'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('text', models.TextField(verbose_name='Text')),
                ('text_html', models.TextField(verbose_name='Text Html')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Created date')),
                ('modified_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Modified date')),
                ('author', models.ForeignKey(related_name='user_comments', to=settings.AUTH_USER_MODEL)),
                ('issue', models.ForeignKey(related_name='comments', to='apptracker.Issue')),
            ],
            options={
                'verbose_name': 'Comment',
                'verbose_name_plural': 'Comments',
                'ordering': ['-pk'],
            },
            bases=(models.Model,),
        ),
    ]
