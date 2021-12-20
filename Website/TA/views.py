# views home

from django.shortcuts import redirect, render
from django.contrib import messages
from produk.models import ProdukDijadwalkan
from produk.forms import  FormProdukDijadwalkan

# Create your views here.
def home(request):
    context = {
        'judul': 'Project Shop SPTM',
        'subjudul': 'Sistem Produksi Terdistribusi Mandiri',
        'konten': '',
        'banner': 'img/banner.png',
    }

    return render(request, 'home.html', context)