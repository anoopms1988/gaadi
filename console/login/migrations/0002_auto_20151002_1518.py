# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import console.login.models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dealer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('phonenumber', models.CharField(max_length=100)),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(null=True, auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('mobilenumber', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('openinghours', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'dealers',
            },
        ),
        migrations.AlterField(
            model_name='company',
            name='description',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='company',
            name='logo',
            field=models.FileField(verbose_name='Upload Logo', blank=True, null=True, upload_to=console.login.models.Company.generate_filename),
        ),
        migrations.AddField(
            model_name='dealer',
            name='company',
            field=models.ForeignKey(to='login.Company'),
        ),
    ]
