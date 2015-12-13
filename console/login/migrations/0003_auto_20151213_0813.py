# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_auto_20151213_0812'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='price',
            field=models.TextField(default='Not available'),
        ),
        migrations.AlterField(
            model_name='car',
            name='description',
            field=models.TextField(),
        ),
    ]
