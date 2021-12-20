# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-12-15 13:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('produk', '0017_auto_20211207_2006'),
        ('engineeringorder', '0005_auto_20211129_0045'),
    ]

    operations = [
        migrations.CreateModel(
            name='MaterialEO',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_materialeo', models.CharField(max_length=255)),
                ('nama_material', models.CharField(max_length=255)),
                ('nama_supplier', models.CharField(blank=True, max_length=255, null=True)),
                ('tanggal_berlaku', models.DateField(blank=True, null=True)),
                ('is_berlaku', models.NullBooleanField(default=True)),
                ('tanggalGanti', models.DateField(blank=True, null=True)),
                ('keterangan', models.TextField(blank=True, null=True)),
                ('penggantiMaterial', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='penggantiMaterial_material_set', to='engineeringorder.MaterialEO')),
                ('penyusun_produk', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='penyusun_produk_material_set', to='engineeringorder.MaterialEO')),
                ('varian_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produk.Produk', to_field='id_varian')),
            ],
        ),
    ]
