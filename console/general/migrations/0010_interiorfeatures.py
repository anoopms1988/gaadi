# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0004_auto_20151016_1750'),
        ('general', '0009_wheel'),
    ]

    operations = [
        migrations.CreateModel(
            name='InteriorFeatures',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('power_steering', models.CharField(default=0, max_length=2, choices=[(1, b'Yes'), (0, b'NO')])),
                ('power_windows', models.CharField(default=0, max_length=2, choices=[(1, b'Yes'), (0, b'NO')])),
                ('anti_pinch', models.CharField(default=0, max_length=2, choices=[(1, b'Yes'), (0, b'NO')])),
                ('air_con', models.CharField(default=0, max_length=2, choices=[(1, b'Yes'), (0, b'NO')])),
                ('audio_system', models.CharField(default=0, max_length=2, choices=[(1, b'Yes'), (0, b'NO')])),
                ('electric_mirrors', models.CharField(default=0, max_length=2, choices=[(1, b'Yes'), (0, b'NO')])),
                ('deffoger', models.CharField(default=0, max_length=2, choices=[(1, b'Yes'), (0, b'NO')])),
                ('leather_seats', models.CharField(default=0, max_length=2, choices=[(1, b'Yes'), (0, b'NO')])),
                ('reversing_camera', models.CharField(default=0, max_length=2, choices=[(1, b'Yes'), (0, b'NO')])),
                ('bluetooth_connectivity', models.CharField(default=0, max_length=2, choices=[(1, b'Yes'), (0, b'NO')])),
                ('cruise_control', models.CharField(default=0, max_length=2, choices=[(1, b'Yes'), (0, b'NO')])),
                ('remote_boot_release', models.CharField(default=0, max_length=2, choices=[(1, b'Yes'), (0, b'NO')])),
                ('chilled_glovebox', models.CharField(default=0, max_length=2, choices=[(1, b'Yes'), (0, b'NO')])),
                ('rear_ac_vents', models.CharField(default=0, max_length=2, choices=[(1, b'Yes'), (0, b'NO')])),
                ('keyless_start_stop_button', models.CharField(default=0, max_length=2, choices=[(1, b'Yes'), (0, b'NO')])),
                ('electric_foldable_mirrors', models.CharField(default=0, max_length=2, choices=[(1, b'Yes'), (0, b'NO')])),
                ('tachometer', models.CharField(default=0, max_length=2, choices=[(1, b'Yes'), (0, b'NO')])),
                ('arm_rest', models.CharField(default=0, max_length=2, choices=[(1, b'Yes'), (0, b'NO')])),
                ('steering_controls', models.CharField(default=0, max_length=2, choices=[(1, b'Yes'), (0, b'NO')])),
                ('driver_info_display', models.CharField(default=0, max_length=2, choices=[(1, b'Yes'), (0, b'NO')])),
                ('foot_rest', models.CharField(default=0, max_length=2, choices=[(1, b'Yes'), (0, b'NO')])),
                ('driver_seat_height_adjust', models.CharField(default=0, max_length=2, choices=[(1, b'Yes'), (0, b'NO')])),
                ('power_seats', models.CharField(default=0, max_length=2, choices=[(1, b'Yes'), (0, b'NO')])),
                ('variant', models.ForeignKey(to='login.Variant')),
            ],
            options={
                'db_table': 'interior_features',
            },
        ),
    ]
