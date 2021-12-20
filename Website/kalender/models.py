from django.db import models

# Create your models here.
# models jam kerja
class JamKerja(models.Model):
    jam_kerja = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return "{}".format(self.jam_kerja)

from django.db.models.deletion import CASCADE

# Create your models here.
# models produk

class KalenderPenjadwalan(models.Model):
    kalender_penjadwalan = models.DateTimeField(blank=True, null=True)
    jam_kerja_id = models.ForeignKey(JamKerja, on_delete=CASCADE)

    def __str__(self):
        return "{}".format(self.kalender_penjadwalan)