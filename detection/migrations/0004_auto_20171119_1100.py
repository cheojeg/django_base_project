# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-19 15:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('detection', '0003_auto_20171118_1244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detection',
            name='latitude',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='detection',
            name='longitude',
            field=models.FloatField(blank=True, null=True),
        ),
    ]