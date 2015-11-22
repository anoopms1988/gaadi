# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0012_safetyfeatures'),
    ]

    operations = [
        migrations.AlterField(
            model_name='safetyfeatures',
            name='abs',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='safetyfeatures',
            name='airbags',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='safetyfeatures',
            name='central_locking',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='safetyfeatures',
            name='child_safety_lock',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='safetyfeatures',
            name='ebd',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='safetyfeatures',
            name='esp',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='safetyfeatures',
            name='hill_control',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='safetyfeatures',
            name='hill_descent',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='safetyfeatures',
            name='immobilizer',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='safetyfeatures',
            name='traction_control',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='safetyfeatures',
            name='wheel_drive',
            field=models.BooleanField(default=True),
        ),
    ]
