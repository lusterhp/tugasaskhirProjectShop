# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-11-28 17:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('engineeringorder', '0003_auto_20211125_0129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='engineeringorder',
            name='material_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produk.Material'),
        ),
    ]
