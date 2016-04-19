# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-19 15:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Analysis_table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('attendance_date', models.DateField(auto_now_add=True)),
                ('working_hrs', models.FloatField()),
                ('login_time', models.DateTimeField()),
                ('logout_time', models.DateTimeField()),
                ('state', models.IntegerField()),
            ],
            options={
                'ordering': ('attendance_date',),
            },
        ),
        migrations.CreateModel(
            name='Attendance_table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('user_id', models.IntegerField()),
            ],
            options={
                'ordering': ('created',),
            },
        ),
    ]
