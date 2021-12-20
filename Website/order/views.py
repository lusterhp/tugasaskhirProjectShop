# views order

from .models import LapakKerja
from django.shortcuts import render
from .models import ProsesKerja
from .forms import FormPenjadwalan, ProsesKerja

# Create your views here.

def list(request):
    jadwal1 = ProsesKerja.objects.all()
    context = {
        'judul': "Project Shop SPTM",
        'subjudul': "Sistem Produksi Terdistribusi Mandiri",
        'heading': "List Jadwal",
        'subheading': "Berikut Adalah List Penjadwalan yang Telah Terdaftar",
        'banner': 'order/img/banner.png',
        'app_css': 'order/css/style.css',
        'nav': [
            ['/' ,'Halaman Utama' ],
            ['/order' ,'List Penjadwalan' ],
            ['/order/form' ,'Form Pendaftaran' ],
        ],
        'Jadwal1':jadwal1,
    }

    return render(request, 'order/list.html', context)

def hasilpost(request):
    hasil1 = ProsesKerja.objects.all()
    context = {
        'Hasil1':hasil1,
    }

    return render(request, 'templates/base2.html', context)

def form(request):
    if request.POST:
        form = FormPenjadwalan(request.POST)
        if form.is_valid():
            form.save()
            form = FormPenjadwalan()
            pesan = "Penjadwalan berhasil didaftarkan"
            context = {
                'judul': 'Project Shop SPTM',
                'subjudul': 'Sistem Produksi Terdistribusi Mandiri',
                'heading': "Form Pendaftaran",
                'subheading': 'Silahkan Mengisi Form untuk Meminta Penjadwalan Produksi',
                'banner': 'order/img/banner.png',
                'app_css': 'order/css/style.css',
                'nav': [
                    ['/' ,'Halaman Utama' ],
                    ['/order' ,'List Penjadwalan' ],
                    ['/order/form' ,'Form Pendaftaran' ],
                ],
                'form':form,
                'pesan':pesan,
            }

            return render(request, 'order/form.html', context)

    else:
        form = FormPenjadwalan()
        context = {
            'judul': 'Project Shop SPTM',
            'subjudul': 'Sistem Produksi Terdistribusi Mandiri',
            'heading': "Form Pendaftaran",
            'subheading': 'Silahkan Mengisi Form untuk Meminta Penjadwalan Produksi',
            'banner': 'order/img/banner.png',
            'app_css': 'order/css/style.css',
            'nav': [
                ['/' ,'Halaman Utama' ],
                ['/order' ,'List Penjadwalan' ],
                ['/order/form' ,'Form Pendaftaran' ],
            ],
            'form':form,
        }

        return render(request, 'order/form.html', context)

