from django.db import models
from django.db.models.deletion import CASCADE

from produk.models import *
from projectshop.models import *

# Create your models here.
# models material

class Material(models.Model):
    varian_id = models.ForeignKey(Produk, on_delete=CASCADE, to_field='id_varian')
    id_material = models.CharField(max_length=255)
    nama_material = models.CharField(max_length=255)
    nama_supplier = models.CharField(max_length=255, blank=True, null=True)
    penyusun_produk = models.ForeignKey('self', on_delete=CASCADE, blank=True, null=True, related_name='penyusun_produk_material_set')
    tanggal_berlaku = models.DateField(blank=True, null=True)
    
    is_berlaku = models.NullBooleanField(default=True, blank=True)
    tanggalGanti = models.DateField(null=True, blank=True)
    keterangan = models.TextField(null=True, blank=True)
    penggantiMaterial = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='penggantiMaterial_material_set')

    def __str__(self):
        return "{}".format(self.id_material)

class Proses(models.Model):
    id_proses = models.CharField(max_length=255)
    nama_proses = models.CharField(max_length=255)
    varian_id = models.ForeignKey(Produk, on_delete=CASCADE, to_field='id_varian')
    material_id = models.ForeignKey(Material, on_delete=CASCADE)
    peralatan_id = models.ManyToManyField(PeralatanKerja)
    grup_id = models.ForeignKey(TipeKerja, on_delete=CASCADE)
    durasi = models.IntegerField()
    tahapan_pengerjaan = models.IntegerField()

    def __str__(self):
        return "{}".format(self.id_proses)