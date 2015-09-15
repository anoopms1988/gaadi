# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0008_auto_20150915_0640'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartype',
            old_name='type',
            new_name='cartype',
        ),
    ]
