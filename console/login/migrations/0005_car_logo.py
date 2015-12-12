# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import console.login.models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0004_auto_20151212_0732'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='logo',
            field=models.FileField(verbose_name='Upload Logo', blank=True, null=True, upload_to=console.login.models.generate_carlogo),
        ),
    ]
