# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-12-15 14:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('engineeringorder', '0008_auto_20211215_2039'),
    ]

    operations = [
        migrations.AddField(
            model_name='materialeo',
            name='kode_eo',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]