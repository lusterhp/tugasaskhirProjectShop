# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-12-01 18:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('produk', '0013_auto_20211129_0044'),
        ('projectshop', '0009_delete_kodeperalatan'),
        ('design', '0012_auto_20211201_2302'),
    ]

    operations = [
        migrations.CreateModel(
            name='Proses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_proses', models.IntegerField(max_length=255)),
                ('nama_proses', models.CharField(max_length=255)),
                ('durasi', models.IntegerField()),
                ('tahapan_pengerjaan', models.IntegerField()),
                ('tipe_pengerjaan', models.IntegerField()),
                ('grup_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projectshop.GrupKerja')),
                ('material_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='design.Material')),
                ('peralatan_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projectshop.PeralatanKerja')),
                ('varian_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produk.Produk', to_field='id_varian')),
            ],
        ),
    ]
