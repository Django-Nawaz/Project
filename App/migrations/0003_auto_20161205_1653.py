# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-12-05 11:23
from __future__ import unicode_literals

from django.db import migrations
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0002_auto_20161205_1649'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='sub_unit',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='chap_id', chained_model_field='chap_id', on_delete=django.db.models.deletion.CASCADE, to='App.Sub_Units'),
        ),
    ]
