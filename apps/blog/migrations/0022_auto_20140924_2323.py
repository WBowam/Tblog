# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0021_auto_20140924_1951'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='disliked_ip',
            field=models.TextField(default=datetime.date(2014, 9, 24), verbose_name='disliked_ip'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='article',
            name='liked_ip',
            field=models.TextField(verbose_name='liked_ip'),
        ),
    ]
