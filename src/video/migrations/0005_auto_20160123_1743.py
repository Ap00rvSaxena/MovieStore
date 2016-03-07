# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0004_video_slug'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='video',
            options={'ordering': ['-create_date', '-updated']},
        ),
        migrations.AlterField(
            model_name='video',
            name='desc',
            field=models.TextField(max_length=400),
        ),
    ]
