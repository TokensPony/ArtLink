# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-11-19 05:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0020_commission_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commission',
            name='user',
        ),
    ]
