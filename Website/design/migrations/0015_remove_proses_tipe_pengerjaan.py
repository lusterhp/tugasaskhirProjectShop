# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-12-02 02:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('design', '0014_auto_20211202_0109'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='proses',
            name='tipe_pengerjaan',
        ),
    ]
