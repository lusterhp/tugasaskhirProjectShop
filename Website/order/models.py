from datetime import datetime
from django.db import models
from produk.models import *
from projectshop.models import *

# Create your models here.

class ProsesKerja(models.Model):
    nama_proses = models.CharField(max_length=255)
    material_id = models.ForeignKey(Material, on_delete=CASCADE, blank=True, null=True)
    peralatankerja_id = models.ForeignKey(PeralatanKerja, on_delete=CASCADE, blank=True, null=True)
    waktu_mulai = models.DateTimeField(null=False, blank=False)
    waktu_selesai = models.DateTimeField(null=False, blank=False)
    produk_id = models.ForeignKey(Produk, on_delete=CASCADE)
    lapakkerja_id = models.ForeignKey(LapakKerja, on_delete=CASCADE)

    def __str__(self):
        return "{}".format(self.nama_proses)

from django.db import models
from django.db.models.deletion import CASCADE
from design.models import Proses

# Create your models here.
# models operasi


class Operasi(models.Model):
    produkdijadwalkan_id = models.ForeignKey(ProdukDijadwalkan, on_delete=CASCADE, blank=True, null=True)
    proses_id = models.ForeignKey(Proses, on_delete=CASCADE, blank=True, null=True)
    grup_id = models.ForeignKey(GrupKerja, on_delete=CASCADE, blank=True, null=True)
    waktu_mulai = models.DateTimeField(blank=True, null=True)
    waktu_selesai = models.DateTimeField(blank=True, null=True)
    status_operasi = models.BooleanField(default=False)

    def __str__(self):
        return f'operasi {self.proses_id} dari pesanan {self.produkdijadwalkan_id} dikerjakan mulai dari {self.waktu_mulai} hingga {self.waktu_selesai}'