# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-12-06 04:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projectshop', '0011_tipekerja'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grupkerja',
            name='kode_grup',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projectshop.TipeKerja'),
        ),
    ]
