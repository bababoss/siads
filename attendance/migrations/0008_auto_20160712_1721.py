# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-12 17:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0007_auto_20160706_1219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='geodata',
            name='device_id',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='geodata',
            name='latitude',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='geodata',
            name='longitude',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='geodata',
            name='user_id',
            field=models.CharField(max_length=100),
        ),
    ]
