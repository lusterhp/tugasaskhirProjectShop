# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-12-06 16:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectshop', '0014_lapakkerja_grup_kerja'),
        ('produk', '0014_auto_20211202_0837'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produkdijadwalkan',
            name='jam_diminta',
        ),
        migrations.RemoveField(
            model_name='produkdijadwalkan',
            name='tanggal_diminta',
        ),
        migrations.AddField(
            model_name='produkdijadwalkan',
            name='deadline_diminta',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.RemoveField(
            model_name='produkdijadwalkan',
            name='lapak_id',
        ),
        migrations.AddField(
            model_name='produkdijadwalkan',
            name='lapak_id',
            field=models.ManyToManyField(to='projectshop.LapakKerja'),
        ),
        migrations.AlterField(
            model_name='produkdijadwalkan',
            name='status_pengerjaan',
            field=models.CharField(choices=[('Selesai', 'Selesai'), ('Berjalan', 'Berjalan'), ('Jadwal Terkonfirmasi', 'Jadwal Terkonfirmasi'), ('Jadwal Belum Dikonfirmasi', 'Jadwal Belum Dikonfirmasi')], default='Jadwal Belum Dikonfirmasi', max_length=200),
        ),
    ]