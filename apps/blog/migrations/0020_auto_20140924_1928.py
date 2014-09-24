# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0019_auto_20140924_1924'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='liked_ip',
            field=models.IPAddressField(verbose_name='Ip'),
        ),
    ]
