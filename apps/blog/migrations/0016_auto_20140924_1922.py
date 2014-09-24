# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_article_liked_ip'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='liked_ip',
            field=models.IPAddressField(verbose_name='Create Time', blank=True),
        ),
    ]
