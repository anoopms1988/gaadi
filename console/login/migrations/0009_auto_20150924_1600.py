# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0008_engine'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='description',
            field=models.CharField(null=True, max_length=100),
        ),
        migrations.AddField(
            model_name='company',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
