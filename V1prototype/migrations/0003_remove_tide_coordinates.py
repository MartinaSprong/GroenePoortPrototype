# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-05-22 11:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('V1prototype', '0002_auto_20170522_1152'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tide',
            name='coordinates',
        ),
    ]
