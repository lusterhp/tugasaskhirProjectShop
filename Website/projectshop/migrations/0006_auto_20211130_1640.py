# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-11-30 09:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projectshop', '0005_auto_20211130_1545'),
    ]

    operations = [
        migrations.RenameField(
            model_name='kodeperalatan',
            old_name='kode_alat',
            new_name='id_alat',
        ),
    ]
