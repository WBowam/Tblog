# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_auto_20140924_1923'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='liked_ip',
            field=models.IPAddressField(null=True, verbose_name='Ip', blank=True),
        ),
    ]
