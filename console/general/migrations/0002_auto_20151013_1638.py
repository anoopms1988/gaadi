# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dimensions',
            name='bootspace',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='dimensions',
            name='kerbweight',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='dimensions',
            name='wheelbase',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
