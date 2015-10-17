# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0004_auto_20151016_1750'),
        ('general', '0003_auto_20151013_1643'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brake',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('rear_brakes', models.CharField(max_length=100)),
                ('front_brakes', models.CharField(max_length=100)),
                ('variant', models.ForeignKey(to='login.Variant')),
            ],
            options={
                'db_table': 'brakes',
            },
        ),
    ]
