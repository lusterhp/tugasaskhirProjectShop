

# models engineering order

from typing import DefaultDict
from django.db import models
from django.db.models.deletion import CASCADE
from design.models import *


# Create your models here.
# models engineering order

class MaterialEO(models.Model):
    kode_eo = models.CharField(max_length=255)
    varian_id = models.ForeignKey(Produk, on_delete=CASCADE, to_field='id_varian')
    id_materialeo = models.CharField(max_length=255)
    nama_material = models.CharField(max_length=255)
    nama_supplier = models.CharField(max_length=255, blank=True, null=True)
    penyusun_produk = models.ForeignKey(Material, on_delete=CASCADE, blank=True, null=True, related_name='penyusun_produk_material_eo')
    tanggal_berlaku = models.DateField(blank=True, null=True)
    
    is_berlaku = models.NullBooleanField(default=True, blank=True)
    tanggalGanti = models.DateField(null=True, blank=True)
    keterangan = models.TextField(null=True, blank=True)
    penggantiMaterial = models.ForeignKey(Material, on_delete=models.CASCADE, null=True, blank=True, related_name='penggantiMaterial_material_eo')

    def __str__(self):
        return "{}".format(self.kode_eo)

class EngineeringOrder(models.Model):
    nama_pengaju = models.CharField(max_length=255)
    tanggal_diajukan = models.DateTimeField(auto_now_add=True)
    is_disetujui = models.BooleanField(default=False)
    tanggal_persetujuan = models.DateTimeField(blank=True, null=True)
    tanggal_berlaku = models.DateTimeField(blank=True, null=True)
    keterangan = models.CharField(max_length=255)
    material_id = models.ForeignKey(Material, on_delete=CASCADE, blank=True, null=True)


    def __str__(self):
        return "{}".format(self.tanggal_diajukan)
