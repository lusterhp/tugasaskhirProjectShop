# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-11-30 08:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectshop', '0003_remove_kesibukanlapak_operasi_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='GrupKerja',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kode_grup', models.CharField(max_length=255)),
                ('nama_grup', models.CharField(max_length=255)),
                ('jumlah_pekerja', models.IntegerField()),
                ('jamkerja_pekerja', models.IntegerField()),
            ],
        ),
    ]