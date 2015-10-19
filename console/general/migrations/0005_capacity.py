# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0004_auto_20151016_1750'),
        ('general', '0004_brake'),
    ]

    operations = [
        migrations.CreateModel(
            name='Capacity',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('seating_capacity', models.PositiveIntegerField(null=True)),
                ('tank_capacity', models.CharField(null=True, blank=True, max_length=100)),
                ('variant', models.ForeignKey(to='login.Variant')),
            ],
            options={
                'db_table': 'capacity',
            },
        ),
    ]
