# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 10, 18, 9, 35, 558478, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
    ]
