# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0007_variant_fuel'),
    ]

    operations = [
        migrations.CreateModel(
            name='Engine',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('torque', models.CharField(max_length=100)),
                ('displacement', models.CharField(max_length=100)),
                ('power', models.CharField(max_length=100)),
                ('cylinders', models.PositiveIntegerField()),
                ('valvespercylinder', models.PositiveIntegerField()),
                ('valvemechanism', models.CharField(max_length=100)),
                ('cyclinderconfiguration', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('variant', models.ForeignKey(to='login.Variant')),
            ],
            options={
                'db_table': 'engines',
            },
        ),
    ]
