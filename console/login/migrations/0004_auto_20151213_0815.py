# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_auto_20151213_0813'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='price',
            field=models.TextField(default=True),
        ),
    ]
