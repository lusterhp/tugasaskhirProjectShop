# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-11-10 12:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projectshop', '0002_kesibukanlapak'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kesibukanlapak',
            name='operasi_id',
        ),
    ]