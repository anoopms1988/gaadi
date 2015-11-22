# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
        ('general', '0011_exteriorfeatures'),
    ]

    operations = [
        migrations.CreateModel(
            name='SafetyFeatures',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('abs', models.BooleanField(default=False)),
                ('airbags', models.BooleanField(default=False)),
                ('immobilizer', models.BooleanField(default=False)),
                ('hill_control', models.BooleanField(default=False)),
                ('central_locking', models.BooleanField(default=False)),
                ('ebd', models.BooleanField(default=False)),
                ('child_safety_lock', models.BooleanField(default=False)),
                ('traction_control', models.BooleanField(default=False)),
                ('hill_descent', models.BooleanField(default=False)),
                ('esp', models.BooleanField(default=False)),
                ('wheel_drive', models.BooleanField(default=False)),
                ('variant', models.ForeignKey(to='login.Variant')),
            ],
            options={
                'db_table': 'safety_features',
            },
        ),
    ]
