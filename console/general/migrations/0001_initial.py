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
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
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
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('seating_capacity', models.PositiveIntegerField(null=True)),
                ('tank_capacity', models.CharField(blank=True, max_length=100, null=True)),
                ('variant', models.ForeignKey(to='login.Variant')),
            ],
            options={
                'db_table': 'capacity',
            },
        ),
        migrations.CreateModel(
            name='Dimensions',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('length', models.CharField(max_length=100)),
                ('width', models.CharField(max_length=100)),
                ('height', models.CharField(max_length=100)),
                ('wheelbase', models.CharField(blank=True, max_length=100, null=True)),
                ('bootspace', models.CharField(blank=True, max_length=100, null=True)),
                ('kerbweight', models.CharField(blank=True, max_length=100, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('variant', models.ForeignKey(to='login.Variant')),
            ],
            options={
                'db_table': 'dimensions',
            },
        ),
        migrations.CreateModel(
            name='InteriorFeatures',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
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
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('mileage_highway', models.CharField(blank=True, max_length=100, null=True)),
                ('mileage_city', models.CharField(blank=True, max_length=100, null=True)),
                ('mileage_overall', models.CharField(blank=True, max_length=100, null=True)),
                ('variant', models.ForeignKey(to='login.Variant')),
            ],
            options={
                'db_table': 'mileage',
            },
        ),
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('showroom_price', models.CharField(blank=True, max_length=100, null=True)),
                ('onroad_price', models.CharField(blank=True, max_length=100, null=True)),
                ('variant', models.ForeignKey(to='login.Variant')),
            ],
            options={
                'db_table': 'price',
            },
        ),
        migrations.CreateModel(
            name='Steering',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('turning_radius', models.CharField(blank=True, max_length=100, null=True)),
                ('steering_type', models.CharField(blank=True, max_length=100, null=True)),
                ('variant', models.ForeignKey(to='login.Variant')),
            ],
            options={
                'db_table': 'steering',
            },
        ),
        migrations.CreateModel(
            name='Wheel',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('wheelsize', models.CharField(blank=True, max_length=100, null=True)),
                ('wheeltype', models.CharField(blank=True, max_length=100, null=True)),
                ('variant', models.ForeignKey(to='login.Variant')),
            ],
            options={
                'db_table': 'wheel',
            },
        ),
    ]
