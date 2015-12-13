# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0004_auto_20151213_0815'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='price',
            field=models.TextField(null=True),
        ),
    ]
