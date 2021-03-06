# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-11-09 14:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('produk', '0002_produkdijadwalkan'),
    ]

    operations = [
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kode_material', models.CharField(max_length=255)),
                ('nama_material', models.CharField(max_length=255)),
                ('nama_supplier', models.CharField(max_length=255)),
                ('tanggal_ditambahkan', models.DateTimeField(blank=True, null=True)),
                ('is_diubah', models.BooleanField(default=False)),
                ('tanggal_material_diubah', models.DateTimeField(blank=True, null=True)),
                ('keterangan', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Proses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_proses', models.CharField(max_length=255)),
                ('kebutuhan_alat', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='material',
            name='proses_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='design.Proses'),
        ),
        migrations.AddField(
            model_name='material',
            name='variant_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produk.Variant'),
        ),
    ]
