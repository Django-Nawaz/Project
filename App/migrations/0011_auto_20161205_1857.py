# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-12-05 13:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0010_auto_20161205_1856'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='class',
            options={'verbose_name': 'Class', 'verbose_name_plural': 'Classes'},
        ),
    ]