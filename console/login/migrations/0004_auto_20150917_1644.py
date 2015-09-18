# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_auto_20150917_1642'),
    ]

    operations = [
        migrations.AddField(
            model_name='variant',
            name='fuel',
            field=models.ForeignKey(default=1, to='login.Fuel'),
        ),
        migrations.AlterField(
            model_name='fuel',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
