# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-11-07 01:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_profile_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='name',
        ),
        migrations.AddField(
            model_name='profile',
            name='artstyle',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AddField(
            model_name='profile',
            name='willdraw',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AddField(
            model_name='profile',
            name='wontdraw',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='profile',
            name='commstatus',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='profile',
            name='description',
            field=models.TextField(blank=True, max_length=1000),
        ),
    ]
