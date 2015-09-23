# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0004_auto_20150917_1644'),
    ]

    operations = [
        migrations.AlterField(
            model_name='variant',
            name='fuel',
            field=models.ForeignKey(to='login.Fuel'),
        ),
    ]
