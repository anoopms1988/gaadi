# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_auto_20150917_1641'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fuel',
            name='name',
            field=models.CharField(max_length=100, blank=True),
        ),
    ]
