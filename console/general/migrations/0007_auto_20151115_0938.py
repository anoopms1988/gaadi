# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0006_auto_20151110_1636'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interiorfeatures',
            name='power_steering',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='interiorfeatures',
            name='power_windows',
            field=models.BooleanField(default=False),
        ),
    ]
