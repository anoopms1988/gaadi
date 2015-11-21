# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0009_auto_20151119_1603'),
    ]

    operations = [
        migrations.AddField(
            model_name='interiorfeatures',
            name='air_con',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='interiorfeatures',
            name='anti_pinch',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='interiorfeatures',
            name='arm_rest',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='interiorfeatures',
            name='audio_system',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='interiorfeatures',
            name='bluetooth_connectivity',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='interiorfeatures',
            name='chilled_glovebox',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='interiorfeatures',
            name='cruise_control',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='interiorfeatures',
            name='deffoger',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='interiorfeatures',
            name='driver_info_display',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='interiorfeatures',
            name='driver_seat_height_adjust',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='interiorfeatures',
            name='electric_foldable_mirrors',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='interiorfeatures',
            name='electric_mirrors',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='interiorfeatures',
            name='foot_rest',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='interiorfeatures',
            name='keyless_start_stop_button',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='interiorfeatures',
            name='leather_seats',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='interiorfeatures',
            name='power_seats',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='interiorfeatures',
            name='rear_ac_vents',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='interiorfeatures',
            name='remote_boot_release',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='interiorfeatures',
            name='reversing_camera',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='interiorfeatures',
            name='steering_controls',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='interiorfeatures',
            name='tachometer',
            field=models.BooleanField(default=False),
        ),
    ]
