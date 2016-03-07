# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0005_auto_20160123_1743'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='movie',
            field=models.FileField(default=datetime.datetime(2016, 1, 23, 13, 23, 54, 644143, tzinfo=utc), upload_to='title'),
            preserve_default=False,
        ),
    ]
