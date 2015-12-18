# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='price',
            name='emi',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='mileage',
            name='variant',
            field=models.ForeignKey(to='login.Variant', related_name='mileage'),
        ),
        migrations.AlterField(
            model_name='price',
            name='variant',
            field=models.ForeignKey(to='login.Variant', related_name='price'),
        ),
    ]
