# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0003_auto_20160111_2358'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='slug',
            field=models.SlugField(unique=True, default=datetime.datetime(2016, 1, 23, 11, 6, 10, 601369, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
