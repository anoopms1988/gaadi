# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0013_auto_20151122_1705'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('user_name', models.CharField(max_length=100)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('mobile', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'users',
            },
        ),
    ]
