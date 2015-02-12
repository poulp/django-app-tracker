# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('title', models.CharField(max_length=140, verbose_name='Title')),
                ('description', models.TextField(verbose_name='Description')),
                ('description_html', models.TextField(verbose_name='Description Html')),
                ('is_closed', models.BooleanField(default=False)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Created date')),
                ('modified_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Modified date')),
            ],
            options={
                'ordering': ['-pk'],
                'verbose_name_plural': 'Issues',
                'verbose_name': 'Issue',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='IssueActivity',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('attribute_changed', models.CharField(max_length=200, verbose_name='Changed')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Created date')),
                ('issue', models.ForeignKey(to='apptracker.Issue', related_name='activity')),
            ],
            options={
                'verbose_name_plural': 'Issue Activities',
                'verbose_name': 'Issue Activity',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Label',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('title', models.CharField(max_length=20, verbose_name='Title')),
                ('slug', models.SlugField(max_length=20, verbose_name='Slug')),
                ('color', models.CharField(default='#2D3E63', max_length=7, verbose_name='Color')),
            ],
            options={
                'ordering': ['color'],
                'verbose_name_plural': 'Labels',
                'verbose_name': 'Label',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=80, verbose_name='Name')),
                ('slug', models.CharField(max_length=80, verbose_name='Slug')),
                ('description', models.CharField(max_length=200, verbose_name='Description')),
                ('repository', models.URLField(blank=True, verbose_name='Repository')),
                ('documentation', models.URLField(blank=True, verbose_name='Documentation')),
            ],
            options={
                'ordering': ['slug'],
                'verbose_name_plural': 'Projects',
                'verbose_name': 'Project',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='label',
            name='project',
            field=models.ForeignKey(to='apptracker.Project', related_name='labels'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='issue',
            name='labels',
            field=models.ManyToManyField(to='apptracker.Label', related_name='issues', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='issue',
            name='owner',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='owned_issues'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='issue',
            name='project',
            field=models.ForeignKey(to='apptracker.Project', related_name='issues'),
            preserve_default=True,
        ),
    ]
