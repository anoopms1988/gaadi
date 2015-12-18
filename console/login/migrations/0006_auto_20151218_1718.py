# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0005_auto_20151213_0816'),
    ]

    operations = [
        migrations.AlterField(
            model_name='engine',
            name='variant',
            field=models.ForeignKey(to='login.Variant', related_name='engine'),
        ),
    ]
