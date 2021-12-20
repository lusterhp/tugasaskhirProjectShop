# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-11-28 17:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('produk', '0010_variant'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_brand', models.CharField(max_length=255)),
                ('nama_brand', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='produk',
            name='id_model',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='produk',
            name='id_variant',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='produk',
            name='nama_atribut',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='produk',
            name='nama_model',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='produk',
            name='nama_variant',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='produk',
            name='nilai_atribut',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='produkdijadwalkan',
            name='produk_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produk.Brand'),
        ),
    ]
