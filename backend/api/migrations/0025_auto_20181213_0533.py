# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-12-13 05:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0024_auto_20181211_2127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='commstatus',
            field=models.CharField(choices=[('Open', 'Open'), ('Closed', 'Closed')], default='', max_length=1000),
        ),
    ]
