# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apptracker', '0003_userproxy'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserProxy',
        ),
    ]
