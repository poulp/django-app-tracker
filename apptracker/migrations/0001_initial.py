# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('is_issue_owner', models.BooleanField(default=False)),
                ('text', models.TextField(verbose_name='Text')),
                ('text_html', models.TextField(verbose_name='Text Html')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Created date')),
                ('modified_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Modified date')),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='user_comments')),
            ],
            options={
                'verbose_name_plural': 'Comments',
                'ordering': ['pk'],
                'verbose_name': 'Comment',
                'default_permissions': ('create', 'edit', 'view'),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=140, verbose_name='Title')),
                ('description', models.TextField(default='', verbose_name='Description', blank=True)),
                ('description_html', models.TextField(verbose_name='Description Html')),
                ('is_closed', models.BooleanField(default=False)),
                ('pull_request', models.URLField(default='', blank=True)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Created date')),
                ('modified_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Modified date')),
            ],
            options={
                'verbose_name_plural': 'Issues',
                'ordering': ['-pk'],
                'verbose_name': 'Issue',
                'default_permissions': ('create', 'edit', 'delete', 'view'),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='IssueActivity',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
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
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=20, verbose_name='Title')),
                ('slug', models.SlugField(max_length=20, verbose_name='Slug')),
                ('color', models.CharField(default='#2D3E63', max_length=7, verbose_name='Color')),
            ],
            options={
                'verbose_name_plural': 'Labels',
                'ordering': ['color'],
                'verbose_name': 'Label',
                'default_permissions': ('create', 'edit', 'delete', 'view'),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=80, verbose_name='Name')),
                ('slug', models.CharField(max_length=80, verbose_name='Slug')),
                ('description', models.CharField(max_length=200, verbose_name='Description')),
                ('repository', models.URLField(verbose_name='Repository', blank=True)),
                ('documentation', models.URLField(verbose_name='Documentation', blank=True)),
            ],
            options={
                'verbose_name_plural': 'Projects',
                'ordering': ['slug'],
                'verbose_name': 'Project',
                'default_permissions': ('create', 'edit', 'delete', 'view'),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TrackerTeam',
            fields=[
                ('group_ptr', models.OneToOneField(auto_created=True, serialize=False, to='auth.Group', primary_key=True, parent_link=True)),
                ('color', models.CharField(default='#2D3E63', max_length=7, verbose_name='Color')),
                ('project', models.ForeignKey(to='apptracker.Project', related_name='teams')),
            ],
            options={
                'verbose_name_plural': 'Teams',
                'default_permissions': ('create', 'edit', 'delete', 'view'),
                'verbose_name': 'Team',
            },
            bases=('auth.group',),
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
        migrations.AddField(
            model_name='comment',
            name='issue',
            field=models.ForeignKey(to='apptracker.Issue', related_name='comments'),
            preserve_default=True,
        ),
    ]
