# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-05-22 12:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('V1prototype', '0003_remove_tide_coordinates'),
    ]

    operations = [
        migrations.AddField(
            model_name='tide',
            name='lat',
            field=models.DecimalField(decimal_places=4, default=0, max_digits=12),
        ),
        migrations.AddField(
            model_name='tide',
            name='lon',
            field=models.DecimalField(decimal_places=4, default=0, max_digits=12),
        ),
    ]