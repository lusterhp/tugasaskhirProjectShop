from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from produk.models import *

# Create your models here.
# models lapak kerja

class TipeKerja(models.Model):
    tipe_grup = models.CharField(max_length=255)

    def __str__(self):
        return "{}".format(self.tipe_grup)

class GrupKerja(models.Model):
    kode_grup = models.ForeignKey(TipeKerja, on_delete=CASCADE)
    nama_grup = models.CharField(max_length=255)
    jumlah_pekerja = models.IntegerField()
    nama_personil = models.CharField(max_length=255)
    jamkerja_pekerja = models.IntegerField()
    aktif_bekerja = models.BooleanField(default=False)

    def __str__(self):
        return "{}".format(self.nama_grup)

class LapakKerja(models.Model):
    kode_lapak = models.CharField(max_length=255)
    nama_lapak = models.CharField(max_length=50)
    aktif_bekerja = models.BooleanField(default=False)
    grup_kerja = models.ManyToManyField(GrupKerja)
    jadwal_lapak = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return "{}".format(self.kode_lapak)

class KesibukanLapak(models.Model):
    lapakkerja_id = models.ForeignKey(LapakKerja, on_delete=CASCADE)

    def __str__(self):
        return "{}".format(self.lapakkerja_id)

class PeralatanKerja(models.Model):
    kode_alat = models.CharField(max_length=255)
    nama_alat = models.CharField(max_length=50)

    def __str__(self):
        return "{}".format(self.kode_alat)

class ProsesKerja(models.Model):
    kode_proses = models.CharField(max_length=255)
    nama_proses = models.CharField(max_length=255)
    peralatan_id = models.ForeignKey(PeralatanKerja, on_delete=CASCADE, related_name='perlatan_id_PeralatanKerja_set')
    grup_id = models.ForeignKey(GrupKerja, on_delete=CASCADE)

    def __str__(self):
        return "{}".format(self.kode_proses)