# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_auto_20140924_1124'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='liked_ip',
            field=models.IPAddressField(null=True, verbose_name='Create Time', blank=True),
            preserve_default=True,
        ),
    ]
