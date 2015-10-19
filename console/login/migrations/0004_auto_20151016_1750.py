# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_auto_20151016_1728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='engine',
            name='cylinders',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='engine',
            name='valvespercylinder',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
