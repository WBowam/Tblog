# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0020_auto_20140924_1928'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='liked_ip',
            field=models.TextField(verbose_name='Ip'),
        ),
    ]
