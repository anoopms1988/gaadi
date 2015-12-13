# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import console.login.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Assistance',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('contact_details', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'db_table': 'road_assistance',
            },
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('logo', models.FileField(null=True, upload_to=console.login.models.generate_carlogo, verbose_name='Upload image', blank=True)),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('description', models.TextField()),
            ],
            options={
                'db_table': 'cars',
            },
        ),
        migrations.CreateModel(
            name='CarType',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('cartype', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'db_table': 'cartypes',
            },
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('logo', models.FileField(null=True, upload_to=console.login.models.generate_filename, verbose_name='Upload Logo', blank=True)),
                ('description', models.TextField()),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'db_table': 'companies',
            },
        ),
        migrations.CreateModel(
            name='Dealer',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('phonenumber', models.CharField(max_length=100)),
                ('mobilenumber', models.CharField(max_length=100)),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('email', models.CharField(max_length=100)),
                ('openinghours', models.CharField(max_length=100)),
                ('token', models.CharField(max_length=100, blank=True)),
                ('company', models.ForeignKey(to='login.Company')),
            ],
            options={
                'db_table': 'dealers',
            },
        ),
        migrations.CreateModel(
            name='Engine',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('torque', models.CharField(max_length=100)),
                ('displacement', models.CharField(max_length=100)),
                ('power', models.CharField(max_length=100)),
                ('cylinders', models.PositiveIntegerField(null=True)),
                ('valvespercylinder', models.PositiveIntegerField(null=True)),
                ('valvemechanism', models.CharField(max_length=100)),
                ('cylinderconfiguration', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'db_table': 'engines',
            },
        ),
        migrations.CreateModel(
            name='Fuel',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'fueltype',
            },
        ),
        migrations.CreateModel(
            name='Variant',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('car', models.ForeignKey(to='login.Car')),
                ('fuel', models.ForeignKey(default=1, to='login.Fuel')),
            ],
            options={
                'db_table': 'variants',
            },
        ),
        migrations.AddField(
            model_name='engine',
            name='variant',
            field=models.ForeignKey(to='login.Variant'),
        ),
        migrations.AddField(
            model_name='car',
            name='cartype',
            field=models.ForeignKey(to='login.CarType'),
        ),
        migrations.AddField(
            model_name='car',
            name='company',
            field=models.ForeignKey(to='login.Company'),
        ),
        migrations.AddField(
            model_name='assistance',
            name='company',
            field=models.ForeignKey(to='login.Company'),
        ),
    ]
