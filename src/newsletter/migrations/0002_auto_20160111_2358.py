# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='signup',
            name='updated',
        ),
        migrations.AlterField(
            model_name='signup',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
