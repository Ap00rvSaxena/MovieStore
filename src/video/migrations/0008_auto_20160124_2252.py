# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import video.models


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0007_auto_20160123_1911'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='desc',
            field=models.TextField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='video',
            name='movie',
            field=models.FileField(null=True, blank=True, upload_to=video.models.upload_location),
        ),
    ]
