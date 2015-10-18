# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0004_auto_20151016_1750'),
        ('general', '0005_capacity'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mileage',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('mileage_highway', models.CharField(blank=True, null=True, max_length=100)),
                ('mileage_city', models.CharField(blank=True, null=True, max_length=100)),
                ('mileage_overall', models.CharField(blank=True, null=True, max_length=100)),
                ('variant', models.ForeignKey(to='login.Variant')),
            ],
            options={
                'db_table': 'mileage',
            },
        ),
    ]
