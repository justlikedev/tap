# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2018-06-09 16:25
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20180609_0343'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reserv',
            name='created_at',
        ),
        migrations.AddField(
            model_name='reserv',
            name='session',
            field=models.DurationField(default=datetime.timedelta(0, 1200)),
        ),
    ]