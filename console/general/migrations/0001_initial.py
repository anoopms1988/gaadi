# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brake',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('rear_brakes', models.CharField(max_length=100)),
                ('front_brakes', models.CharField(max_length=100)),
                ('variant', models.ForeignKey(to='login.Variant')),
            ],
            options={
                'db_table': 'brakes',
            },
        ),
        migrations.CreateModel(
            name='Capacity',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('seating_capacity', models.PositiveIntegerField(null=True)),
                ('tank_capacity', models.CharField(max_length=100, null=True, blank=True)),
                ('variant', models.ForeignKey(to='login.Variant')),
            ],
            options={
                'db_table': 'capacity',
            },
        ),
        migrations.CreateModel(
            name='Dimensions',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('length', models.CharField(max_length=100)),
                ('width', models.CharField(max_length=100)),
                ('height', models.CharField(max_length=100)),
                ('wheelbase', models.CharField(max_length=100, null=True, blank=True)),
                ('bootspace', models.CharField(max_length=100, null=True, blank=True)),
                ('kerbweight', models.CharField(max_length=100, null=True, blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('variant', models.ForeignKey(to='login.Variant')),
            ],
            options={
                'db_table': 'dimensions',
            },
        ),
        migrations.CreateModel(
            name='ExteriorFeatures',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
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
        migrations.CreateModel(
            name='InteriorFeatures',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('power_steering', models.BooleanField(default=False)),
                ('power_windows', models.BooleanField(default=False)),
                ('anti_pinch', models.BooleanField(default=False)),
                ('air_con', models.BooleanField(default=False)),
                ('audio_system', models.BooleanField(default=False)),
                ('electric_mirrors', models.BooleanField(default=False)),
                ('deffoger', models.BooleanField(default=False)),
                ('leather_seats', models.BooleanField(default=False)),
                ('reversing_camera', models.BooleanField(default=False)),
                ('bluetooth_connectivity', models.BooleanField(default=False)),
                ('cruise_control', models.BooleanField(default=False)),
                ('remote_boot_release', models.BooleanField(default=False)),
                ('chilled_glovebox', models.BooleanField(default=False)),
                ('rear_ac_vents', models.BooleanField(default=False)),
                ('keyless_start_stop_button', models.BooleanField(default=False)),
                ('electric_foldable_mirrors', models.BooleanField(default=False)),
                ('tachometer', models.BooleanField(default=False)),
                ('arm_rest', models.BooleanField(default=False)),
                ('steering_controls', models.BooleanField(default=False)),
                ('driver_info_display', models.BooleanField(default=False)),
                ('foot_rest', models.BooleanField(default=False)),
                ('driver_seat_height_adjust', models.BooleanField(default=False)),
                ('power_seats', models.BooleanField(default=False)),
                ('variant', models.ForeignKey(to='login.Variant')),
            ],
            options={
                'db_table': 'interior_features',
            },
        ),
        migrations.CreateModel(
            name='Mileage',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('mileage_highway', models.CharField(max_length=100, null=True, blank=True)),
                ('mileage_city', models.CharField(max_length=100, null=True, blank=True)),
                ('mileage_overall', models.CharField(max_length=100, null=True, blank=True)),
                ('variant', models.ForeignKey(to='login.Variant')),
            ],
            options={
                'db_table': 'mileage',
            },
        ),
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('showroom_price', models.CharField(max_length=100, null=True, blank=True)),
                ('onroad_price', models.CharField(max_length=100, null=True, blank=True)),
                ('variant', models.ForeignKey(to='login.Variant')),
            ],
            options={
                'db_table': 'price',
            },
        ),
        migrations.CreateModel(
            name='SafetyFeatures',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('abs', models.BooleanField(default=True)),
                ('airbags', models.BooleanField(default=True)),
                ('immobilizer', models.BooleanField(default=True)),
                ('hill_control', models.BooleanField(default=True)),
                ('central_locking', models.BooleanField(default=True)),
                ('ebd', models.BooleanField(default=True)),
                ('child_safety_lock', models.BooleanField(default=True)),
                ('traction_control', models.BooleanField(default=True)),
                ('hill_descent', models.BooleanField(default=True)),
                ('esp', models.BooleanField(default=True)),
                ('wheel_drive', models.BooleanField(default=True)),
                ('variant', models.ForeignKey(to='login.Variant')),
            ],
            options={
                'db_table': 'safety_features',
            },
        ),
        migrations.CreateModel(
            name='Steering',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('turning_radius', models.CharField(max_length=100, null=True, blank=True)),
                ('steering_type', models.CharField(max_length=100, null=True, blank=True)),
                ('variant', models.ForeignKey(to='login.Variant')),
            ],
            options={
                'db_table': 'steering',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('user_name', models.CharField(max_length=100, null=True, blank=True)),
                ('first_name', models.CharField(max_length=100, null=True, blank=True)),
                ('last_name', models.CharField(max_length=100, null=True, blank=True)),
                ('email', models.CharField(max_length=100, null=True, blank=True)),
                ('gender', models.CharField(max_length=100, null=True, blank=True)),
                ('password', models.CharField(max_length=100, null=True, blank=True)),
                ('city', models.CharField(max_length=100, null=True, blank=True)),
                ('mobile', models.CharField(max_length=100, null=True, blank=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'users',
            },
        ),
        migrations.CreateModel(
            name='Wheel',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('wheelsize', models.CharField(max_length=100, null=True, blank=True)),
                ('wheeltype', models.CharField(max_length=100, null=True, blank=True)),
                ('variant', models.ForeignKey(to='login.Variant')),
            ],
            options={
                'db_table': 'wheel',
            },
        ),
    ]
