# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-06 11:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0005_auto_20160430_1100'),
    ]

    operations = [
        migrations.CreateModel(
            name='Geodata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('time_stamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
