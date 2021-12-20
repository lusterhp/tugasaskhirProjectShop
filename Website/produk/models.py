from django.db import models
from django.db.models.deletion import CASCADE
from projectshop.models import *
from projectshop.models import LapakKerja
# Create your models here.

class Brand(models.Model):
    id_brand = models.CharField(max_length=255)
    nama_brand = models.CharField(max_length=255)

    def __str__(self):
        return "{}".format(self.id_brand)

class Model(models.Model):
    id_model = models.CharField(max_length=255)
    nama_model = models.CharField(max_length=255)

    def __str__(self):
        return "{}".format(self.id_model)

class Variant(models.Model):
    id_varian = models.CharField(max_length=255, unique=True)
    nama_varian = models.CharField(max_length=255)
    nama_atribut = models.CharField(max_length=255)
    nilai_atribut = models.CharField(max_length=255)

    def __str__(self):
        return "{}".format(self.id_varian)

class Produk(models.Model):
    id_brand = models.CharField(max_length=255)
    nama_brand = models.CharField(max_length=255)
    id_model = models.CharField(max_length=255)
    nama_model = models.CharField(max_length=255)
    id_varian = models.CharField(max_length=255, unique=True)
    nama_varian = models.CharField(max_length=255)
    nama_atribut = models.CharField(max_length=255)
    nilai_atribut = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.id_brand}-{self.id_model}-{self.id_varian}'

class Material(models.Model):
    nama_material = models.CharField(max_length=255)
    nama_supplier = models.CharField(max_length=255)
    penyusun_produk = models.CharField(max_length=255)
    is_diubah = models.BooleanField(default=False)
    tanggal_material_diubah = models.DateField(blank=True, null=True)
    keterangan = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return "{}".format(self.nama_material)

class ProdukDijadwalkan(models.Model):
    id_pesanan = models.CharField(max_length=255)
    nama_pesanan = models.CharField(max_length=255)
    produk_id = models.ForeignKey(Produk, on_delete=CASCADE)
    lapak_id = models.ForeignKey(LapakKerja, on_delete=CASCADE, blank=True, null=True)
    deadline_diminta = models.DateTimeField(blank=True, null=True)
    status_CHOICES = [
        ('Selesai', 'Selesai'),
        ('Berjalan', 'Berjalan'),
        ('Jadwal Terkonfirmasi', 'Jadwal Terkonfirmasi'),
        ('Jadwal Belum Dikonfirmasi', 'Jadwal Belum Dikonfirmasi'),
    ]
    status_pengerjaan = models.CharField(default='Jadwal Belum Dikonfirmasi', max_length=200, choices=status_CHOICES)

    def __str__(self):
        return "{}".format(self.id_pesanan)

