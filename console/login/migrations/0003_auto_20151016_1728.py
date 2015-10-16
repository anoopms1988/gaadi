# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_auto_20151013_1614'),
    ]

    operations = [
        migrations.RenameField(
            model_name='engine',
            old_name='cyclinderconfiguration',
            new_name='cylinderconfiguration',
        ),
    ]
