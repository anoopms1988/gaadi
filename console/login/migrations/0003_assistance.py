# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_auto_20151002_1518'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assistance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('contact_details', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('company', models.ForeignKey(to='login.Company')),
            ],
            options={
                'db_table': 'road_assistance',
            },
        ),
    ]
