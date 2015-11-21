# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
        ('general', '0010_auto_20151120_1618'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExteriorFeatures',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('keyless_entry', models.BooleanField(default=False)),
                ('rear_wiper', models.BooleanField(default=False)),
                ('rain_sensing_wipers', models.BooleanField(default=False)),
                ('alloy_wheels', models.BooleanField(default=False)),
                ('roof_rails', models.BooleanField(default=False)),
                ('projector_lamps', models.BooleanField(default=False)),
                ('fog_lights', models.BooleanField(default=False)),
                ('moon_roof', models.BooleanField(default=False)),
                ('auto_headlamps', models.BooleanField(default=False)),
                ('steel_rims', models.BooleanField(default=False)),
                ('rear_spoiler', models.BooleanField(default=False)),
                ('chrome_grille', models.BooleanField(default=False)),
                ('daytime_running_lamps', models.BooleanField(default=False)),
                ('variant', models.ForeignKey(to='login.Variant')),
            ],
            options={
                'db_table': 'exterior_features',
            },
        ),
    ]
