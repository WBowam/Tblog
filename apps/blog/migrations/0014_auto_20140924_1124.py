# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20140922_2024'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='like_times',
            field=models.IntegerField(default=1),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='article',
            name='summary',
            field=models.TextField(error_messages={b'min_length': 'At least %(limit_value)d word,please!(it has %(show_value)d).'}, verbose_name='Summary', validators=[django.core.validators.MinLengthValidator(30)]),
        ),
    ]
