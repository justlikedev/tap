# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2018-06-09 03:43
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20180609_0306'),
    ]

    operations = [
        migrations.AddField(
            model_name='reserv',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2018, 6, 9, 3, 43, 15, 71946, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reserv',
            name='finished',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='reserv',
            name='is_paid',
            field=models.BooleanField(default=False),
        ),
    ]
