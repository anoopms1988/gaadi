# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0004_auto_20151016_1750'),
        ('general', '0007_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Steering',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('turning_radius', models.CharField(null=True, max_length=100, blank=True)),
                ('steering_type', models.CharField(null=True, max_length=100, blank=True)),
                ('variant', models.ForeignKey(to='login.Variant')),
            ],
            options={
                'db_table': 'steering',
            },
        ),
    ]
