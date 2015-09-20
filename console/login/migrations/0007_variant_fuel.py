# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0006_remove_variant_fuel'),
    ]

    operations = [
        migrations.AddField(
            model_name='variant',
            name='fuel',
            field=models.ForeignKey(to='login.Fuel', default=1),
        ),
    ]
