# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0005_auto_20150914_1030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='company',
            field=models.ForeignKey(to='login.Company', choices=[(b'1', b'Honda')]),
        ),
    ]
