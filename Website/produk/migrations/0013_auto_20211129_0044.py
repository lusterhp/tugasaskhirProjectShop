# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-11-28 17:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produk', '0012_auto_20211129_0011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produk',
            name='id_varian',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
