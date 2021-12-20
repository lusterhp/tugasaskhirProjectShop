
import datetime
from projectshop.models import LapakKerja
from order.models import *

def cek_availibilitas(lapakkerja, waktu_mulai, waktu_selesai):
    avail_list=[]
    penjadwalan_list=Operasi.objects.filter(lapakkerja_id=lapakkerja)
    for penjadwalan in penjadwalan_list:
        if penjadwalan.waktu_mulai > waktu_selesai or penjadwalan.waktu_selesai < waktu_mulai:
            avail_list.append(True)
        else:
            avail_list.append(False)
    return all(avail_list)