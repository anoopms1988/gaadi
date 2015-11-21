# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0007_auto_20151115_0938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interiorfeatures',
            name='power_steering',
            field=models.NullBooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='interiorfeatures',
            name='power_windows',
            field=models.NullBooleanField(default=False),
        ),
    ]