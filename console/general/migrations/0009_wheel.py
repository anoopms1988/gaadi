# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0004_auto_20151016_1750'),
        ('general', '0008_steering'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wheel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('wheelsize', models.CharField(null=True, max_length=100, blank=True)),
                ('wheeltype', models.CharField(null=True, max_length=100, blank=True)),
                ('variant', models.ForeignKey(to='login.Variant')),
            ],
            options={
                'db_table': 'wheel',
            },
        ),
    ]
