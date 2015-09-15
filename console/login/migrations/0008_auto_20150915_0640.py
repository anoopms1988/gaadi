# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0007_auto_20150914_1110'),
    ]

    operations = [
        migrations.RenameField(
            model_name='car',
            old_name='type',
            new_name='cartype',
        ),
    ]
