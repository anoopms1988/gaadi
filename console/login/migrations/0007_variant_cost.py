# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0006_auto_20151218_1718'),
    ]

    operations = [
        migrations.AddField(
            model_name='variant',
            name='cost',
            field=models.CharField(null=True, max_length=100, blank=True),
        ),
    ]
