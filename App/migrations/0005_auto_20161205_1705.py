# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-12-05 11:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0004_auto_20161205_1702'),
    ]

    operations = [
        migrations.AlterField(
            model_name='concepts',
            name='concept',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='sub_units',
            name='sub_unit',
            field=models.CharField(max_length=40),
        ),
    ]
