# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-12-06 04:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectshop', '0009_delete_kodeperalatan'),
    ]

    operations = [
        migrations.AddField(
            model_name='grupkerja',
            name='aktif_bekerja',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='grupkerja',
            name='nama_personil',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]