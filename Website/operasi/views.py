
# Create your views here.

# views operasi

from django.forms.forms import Form
from operasi.models import *
from django.contrib import messages
from django.shortcuts import redirect, render
from django.views.generic import ListView, FormView
from design.models import *
from produk.fungsi_penjadwalan.availibility import *
from projectshop.models import *
from django.http import HttpResponse

def homeoperasi(request):
    context = {
        'judul': "Project Shop SPTM",
        'subjudul': "Sistem Produksi Terdistribusi Mandiri",
        'heading': "Produksi",
        'subheading': "Silahkan Memilih Salah Satu Tautan Produksi",
        'banner': 'order/img/banner.png',
        'app_css': 'order/css/style.css',
    }

    return render(request, 'home-operasi.html', context)

def lihatmaterial(request):
    lihat1 = Proses.objects.all()
    lihat2 = Material.objects.all()
    context = {
        'judul': "Project Shop SPTM",
        'subjudul': "Sistem Produksi Terdistribusi Mandiri",
        'heading': "List Design",
        'subheading': "Berikut Adalah List Design",
        'banner': 'order/img/banner.png',
        'app_css': 'order/css/style.css',
        'nav': [
            ['/operasi' ,'List Jadwal Operasi' ],
        ],
        'lihat1' : lihat1,
        'lihat2' : lihat2,
    }
    return render(request, 'lihatmaterial.html', context)
