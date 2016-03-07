# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0002_auto_20160111_2358'),
    ]

    operations = [
        migrations.AddField(
            model_name='signup',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 11, 18, 30, 44, 838871, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='signup',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
