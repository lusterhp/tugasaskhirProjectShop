# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-11-10 12:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projectshop', '0003_remove_kesibukanlapak_operasi_id'),
        ('operasi', '0002_auto_20211110_1833'),
    ]

    operations = [
        migrations.AddField(
            model_name='operasi',
            name='lapakkerja_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='projectshop.LapakKerja'),
        ),
    ]
