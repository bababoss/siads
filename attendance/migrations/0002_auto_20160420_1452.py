# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-20 09:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='analysis_table',
            name='login_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='analysis_table',
            name='logout_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]