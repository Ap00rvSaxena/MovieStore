# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import video.models


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0006_video_movie'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='height_field',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='video',
            name='image',
            field=models.ImageField(height_field='height_field', width_field='width_field', blank=True, upload_to=video.models.upload_location, null=True),
        ),
        migrations.AddField(
            model_name='video',
            name='width_field',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='video',
            name='movie',
            field=models.FileField(upload_to=video.models.upload_location),
        ),
    ]
