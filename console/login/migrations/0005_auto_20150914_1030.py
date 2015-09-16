# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0004_car'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='description',
            field=models.CharField(max_length=100, blank=True),
        ),
    ]
