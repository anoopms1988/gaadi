# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dimensions',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('length', models.CharField(max_length=100)),
                ('width', models.CharField(max_length=100)),
                ('height', models.CharField(max_length=100)),
                ('wheelbase', models.CharField(max_length=100)),
                ('bootspace', models.CharField(max_length=100)),
                ('kerbweight', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('variant', models.ForeignKey(to='login.Variant')),
            ],
            options={
                'db_table': 'dimensions',
            },
        ),
    ]
