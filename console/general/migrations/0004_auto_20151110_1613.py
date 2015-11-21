# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0003_auto_20151103_1728'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='interiorfeatures',
            name='air_con',
        ),
        migrations.RemoveField(
            model_name='interiorfeatures',
            name='anti_pinch',
        ),
        migrations.RemoveField(
            model_name='interiorfeatures',
            name='arm_rest',
        ),
        migrations.RemoveField(
            model_name='interiorfeatures',
            name='audio_system',
        ),
        migrations.RemoveField(
            model_name='interiorfeatures',
            name='bluetooth_connectivity',
        ),
        migrations.RemoveField(
            model_name='interiorfeatures',
            name='chilled_glovebox',
        ),
        migrations.RemoveField(
            model_name='interiorfeatures',
            name='cruise_control',
        ),
        migrations.RemoveField(
            model_name='interiorfeatures',
            name='deffoger',
        ),
        migrations.RemoveField(
            model_name='interiorfeatures',
            name='driver_info_display',
        ),
        migrations.RemoveField(
            model_name='interiorfeatures',
            name='driver_seat_height_adjust',
        ),
        migrations.RemoveField(
            model_name='interiorfeatures',
            name='electric_foldable_mirrors',
        ),
        migrations.RemoveField(
            model_name='interiorfeatures',
            name='electric_mirrors',
        ),
        migrations.RemoveField(
            model_name='interiorfeatures',
            name='foot_rest',
        ),
        migrations.RemoveField(
            model_name='interiorfeatures',
            name='keyless_start_stop_button',
        ),
        migrations.RemoveField(
            model_name='interiorfeatures',
            name='leather_seats',
        ),
        migrations.RemoveField(
            model_name='interiorfeatures',
            name='power_seats',
        ),
        migrations.RemoveField(
            model_name='interiorfeatures',
            name='rear_ac_vents',
        ),
        migrations.RemoveField(
            model_name='interiorfeatures',
            name='remote_boot_release',
        ),
        migrations.RemoveField(
            model_name='interiorfeatures',
            name='reversing_camera',
        ),
        migrations.RemoveField(
            model_name='interiorfeatures',
            name='steering_controls',
        ),
        migrations.RemoveField(
            model_name='interiorfeatures',
            name='tachometer',
        ),
    ]
