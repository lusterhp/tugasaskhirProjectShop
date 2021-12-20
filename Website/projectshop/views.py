# views projectshop

from typing import ContextManager
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
from .forms import *

# Create your views here.

def listlapak(request):
    listlapak = LapakKerja.objects.all()
    context = {
        'judul': 'Project Shop SPTM',
        'subjudul': 'Sistem Produksi Terdistribusi Mandiri',
        'heading': 'List Lapak',
        'subheading': "Berikut Merupakan List Lapak yang Telah Terdaftar",
        'banner': 'about/img/banner.png',
        'app_css': 'order/css/style.css',
        'list1':listlapak,
    }

    return render(request, 'projectshop/listlapak.html', context)

def listgrup(request):
    listgrup = GrupKerja.objects.all()
    context = {
        'judul': 'Project Shop SPTM',
        'subjudul': 'Sistem Produksi Terdistribusi Mandiri',
        'heading': 'List Grup Kerja',
        'subheading': "Berikut Merupakan List Grup Kerja yang Telah Terdaftar",
        'banner': 'about/img/banner.png',
        'app_css': 'order/css/style.css',
        'list1':listgrup,
    }

    return render(request, 'projectshop/listgrup.html', context)

def listpp(request):
    listproses = PeralatanKerja.objects.all()
    context = {
        'judul': 'Project Shop SPTM',
        'subjudul': 'Sistem Produksi Terdistribusi Mandiri',
        'heading': 'List Proses dan Peralatan',
        'subheading': "Berikut Merupakan List Proses dan Peralatan yang Telah Terdaftar",
        'banner': 'about/img/banner.png',
        'app_css': 'order/css/style.css',
        'list1':listproses,
    }

    return render(request, 'projectshop/listpp.html', context)

def listasset(request):
    listlapak = LapakKerja.objects.all()
    listgrup = GrupKerja.objects.all()
    listproses = PeralatanKerja.objects.all()
    context = {
        'judul': 'Project Shop SPTM',
        'subjudul': 'Sistem Produksi Terdistribusi Mandiri',
        'heading': 'List Asset',
        'subheading': "Berikut Merupakan List Asset yang Telah Terdaftar",
        'banner': 'about/img/banner.png',
        'app_css': 'order/css/style.css',
        'list1':listlapak,
        'list2':listgrup,
        'list3':listproses,
    }

    return render(request, 'projectshop/listasset.html', context)

def asset(request):
    context = {
        'judul': 'Project Shop SPTM',
        'subjudul': 'Sistem Produksi Terdistribusi Mandiri',
        'heading': "Project Shop",
        'subheading': "Silahkan Memilih Salah Satu Tautan Project Shop",
        'banner': 'about/img/banner.png',
        'app_css': 'order/css/style.css',
    }

    return render(request, 'projectshop/asset.html', context)

def delete(request, hapus_id):
    LapakKerja.objects.filter(id=hapus_id).delete()
    return redirect('listasset')

def deletegrup(request, hapusgrup_id):
    GrupKerja.objects.filter(id=hapusgrup_id).delete()
    return redirect('listasset')

def deletealat(request, hapusalat_id):
    PeralatanKerja.objects.filter(id=hapusalat_id).delete()
    return redirect('listasset')

def update1(request, update1_id):
    produk_update1 = LapakKerja.objects.get(id=update1_id)
    template = 'projectshop/ubah-lapak.html'
    if request.POST:
        form = FormLapak(request.POST, instance=produk_update1)
        if form.is_valid:
            form.save()
            messages.success(request, "Data berhasil diperbaharui!")
            return redirect(update1, update1_id=update1_id)
    else:
        form = FormLapak(instance=produk_update1)
        konteks = {
            'judul': "Project Shop SPTM",
            'subjudul': "Sistem Produksi Terdistribusi Mandiri",
            'heading': "Form Pembaharuan Lapak Kerja",
            'subheading': "Berikut Adalah Form Pembaharuan Lapak Kerja",
            'banner': 'order/img/banner.png',
            'app_css': 'order/css/style.css',
            'nav': [
                ['/' ,'Halaman Utama' ],
                ['/projectshop' ,'List Lapak Kerja' ],
                ['/projectshop/tambah-lapak' ,'Tambah Lapak Kerja' ],
            ],
            'form':form,
            'produk':produk_update1,
        }
    return render(request, template, konteks)

def form(request):
    context = {
        'judul': 'Project Shop SPTM',
        'subjudul': 'Sistem Produksi Terdistribusi Mandiri',
        'heading': "Penambahan Lapak Kerja",
        'subheading': "Silahkan memilih tautan untuk menambahkan asset",
        'banner': 'about/img/banner.png',
        'app_css': 'order/css/style.css',
        'nav': [
            ['/' ,'Halaman Utama' ],
            ['/projectshop' ,'List Lapak Kerja' ],
            ['/projectshop/tambah-lapak' ,'Tambah Lapak Kerja' ],
        ],
    }

    return render(request, 'projectshop/form.html', context)

def form1(request):
    if request.POST:
        form1 = FormLapak(request.POST)
        if  form1.is_valid():
            form1.save()
            form1 = FormLapak()
            pesan = "Lapak berhasil ditambahkan"
            context = {
                'judul': 'Project Shop SPTM',
                'subjudul': 'Sistem Produksi Terdistribusi Mandiri',
                'heading': "Form Penambahan Asset",
                'subheading': "Silahkan Mengisi Form untuk Menambahkan Lapak",
                'banner': 'about/img/banner.png',
                'app_css': 'order/css/style.css',
                'lapak':form1,
                'pesan' : pesan,
                    }
            return render(request, 'projectshop/form1.html', context)

    else:
        form1 = FormLapak()
        context = {
            'judul': 'Project Shop SPTM',
            'subjudul': 'Sistem Produksi Terdistribusi Mandiri',
            'heading': "Form Penambahan Asset",
            'subheading': "Silahkan Mengisi Form untuk Menambahkan Asset",
            'banner': 'about/img/banner.png',
            'app_css': 'order/css/style.css',
            'lapak':form1,
        }

        return render(request, 'projectshop/form1.html', context)

def updategrup(request, updategrup_id):
    grup_update = GrupKerja.objects.get(id=updategrup_id)
    template = 'projectshop/ubah-grup.html'
    if request.POST:
        form = FormGrup(request.POST, instance=grup_update)
        if form.is_valid():
            form.save()
            messages.success(request, "Data berhasil diperbaharui!")
            return redirect(updategrup, updategrup_id=updategrup_id)

    else:
        form = FormGrup(instance=grup_update)
        konteks = {
            'judul': 'Project Shop SPTM',
            'subjudul': 'Sistem Produksi Terdistribusi Mandiri',
            'heading': "Form Pembaharuan Data Grup Kerja",
            'subheading': "Silahkan Mengisi Form untuk Memperbaharui Data Grup Kerja",
            'banner': 'about/img/banner.png',
            'app_css': 'order/css/style.css',
            'grup':form,
            'produk':grup_update
        }
    return render(request, template, konteks)

def updateproses(request, updateproses_id):
    proses_update = ProsesKerja.objects.get(id=updateproses_id)
    template = 'projectshop/ubah-proses.html'
    if request.POST:
        form = FormProses(request.POST, instance=proses_update)
        if form.is_valid():
            form.save()
            messages.success(request, "Data berhasil diperbaharui!")
            return redirect(updateproses, updateproses_id=updateproses_id)

    else:
        form = FormProses(instance=proses_update)
        konteks = {
            'judul': 'Project Shop SPTM',
            'subjudul': 'Sistem Produksi Terdistribusi Mandiri',
            'heading': "Form Pembaharuan Proses",
            'subheading': "Silahkan Mengisi Form untuk Memperbaharui Proses",
            'banner': 'about/img/banner.png',
            'app_css': 'order/css/style.css',
            'proses':form,
            'produk':proses_update
        }
    return render(request, template, konteks)

def updatealat(request, updatealat_id):
    alat_update = PeralatanKerja.objects.get(id=updatealat_id)
    template = 'projectshop/ubah-alat.html'
    if request.POST:
        form = FormAlat(request.POST, instance=alat_update)
        if form.is_valid():
            form.save()
            messages.success(request, "Data berhasil diperbaharui!")
            return redirect(updatealat, updatealat_id=updatealat_id)

    else:
        form = FormAlat(instance=alat_update)
        konteks = {
            'judul': 'Project Shop SPTM',
            'subjudul': 'Sistem Produksi Terdistribusi Mandiri',
            'heading': "Form Pembaharuan Peralatan Kerja",
            'subheading': "Silahkan Mengisi Form untuk Memperbaharui Peralatan Kerja",
            'banner': 'about/img/banner.png',
            'app_css': 'order/css/style.css',
            'alat':form,
            'produk':alat_update
        }
    return render(request, template, konteks)

    # form1 = FormLapak()
    # if request.method == 'POST':
    #     LapakKerja.objects.create(
    #         nama_lapak = request.POST.get('nama_lapak'),
    #         availabilitas = request.POST.get('availabilitas'),
    #     )

    # context = {
    #     'judul': 'Project Shop SPTM',
    #     'subjudul': 'Sistem Produksi Terdistribusi Mandiri',
    #     'heading': "Form Penambahan Asset",
    #     'subheading': "Silahkan Mengisi Form untuk Menambahkan Lapak",
    #     'banner': 'about/img/banner.png',
    #     'app_css': 'order/css/style.css',
    #     'nav': [
    #         ['/' ,'Halaman Utama' ],
    #         ['/projectshop/tambah-asset' ,'Tambah Asset' ],
    #         ['/projectshop/tambah-lapak' ,'Tambah Lapak' ],
    #         ['/projectshop/tambah-kodealat' ,'Tambah Kode Alat' ],
    #         ['/projectshop/tambah-peralatan' ,'Tambah Peralatan' ],
    #     ],
    #     'lapak':form1,
    # }
    # return render(request, 'projectshop/form1.html', context)

    # form2 = FormKode()
    # if request.method == 'POST':
    #     KodePeralatan.objects.create(
    #     kode_alat = request.POST.get('kode_alat'),
    #     )

    # context = {
    #     'judul': 'Project Shop SPTM',
    #     'subjudul': 'Sistem Produksi Terdistribusi Mandiri',
    #     'heading': "Form Penambahan Asset",
    #     'subheading': "Silahkan Mengisi Form untuk Menambahkan Kode Alat",
    #     'banner': 'about/img/banner.png',
    #     'app_css': 'order/css/style.css',
    #     'nav': [
    #         ['/' ,'Halaman Utama' ],
    #         ['/projectshop/tambah-asset' ,'Tambah Asset' ],
    #         ['/projectshop/tambah-lapak' ,'Tambah Lapak' ],
    #         ['/projectshop/tambah-kodealat' ,'Tambah Kode Alat' ],
    #         ['/projectshop/tambah-peralatan' ,'Tambah Peralatan' ],
    #     ],
    #     'kode':form2,
    # }
    # return render(request, 'projectshop/form2.html', context)

def form3(request):
    if request.POST:
        form3 = FormAlat(request.POST)
        if form3.is_valid():
            form3.save()
            form3 = FormAlat()
            pesan = "Alat berhasil ditambahkan"
            context = {
                'judul': 'Project Shop SPTM',
                'subjudul': 'Sistem Produksi Terdistribusi Mandiri',
                'heading': "Form Penambahan Asset",
                'subheading': "Silahkan Mengisi Form untuk Menambahkan Peralatan",
                'banner': 'about/img/banner.png',
                'app_css': 'order/css/style.css',
                'alat':form3,
                'pesan' : pesan,
            }
            return render(request, 'projectshop/form3.html', context)

    else:
        form3 = FormAlat()
        context = {
            'judul': 'Project Shop SPTM',
            'subjudul': 'Sistem Produksi Terdistribusi Mandiri',
            'heading': "Form Penambahan Asset",
            'subheading': "Silahkan Mengisi Form untuk Menambahkan Peralatan",
            'banner': 'about/img/banner.png',
            'app_css': 'order/css/style.css',
            'alat':form3,
        }

        return render(request, 'projectshop/form3.html', context)

def form4(request):
    if request.POST:
        form4 = FormGrup(request.POST)
        if form4.is_valid():
            form4.save()
            form4 = FormGrup()
            pesan = "Grup Kerja berhasil ditambahkan"
            context = {
                'judul': 'Project Shop SPTM',
                'subjudul': 'Sistem Produksi Terdistribusi Mandiri',
                'heading': "Form Penambahan Asset",
                'subheading': "Silahkan Mengisi Form untuk Menambahkan Grup Kerja",
                'banner': 'about/img/banner.png',
                'app_css': 'order/css/style.css',
                'form':form4,
                'pesan' : pesan,
            }
            return render(request, 'projectshop/form4.html', context)

    else:
        form4 = FormGrup()
        context = {
            'judul': 'Project Shop SPTM',
            'subjudul': 'Sistem Produksi Terdistribusi Mandiri',
            'heading': "Form Penambahan Asset",
            'subheading': "Silahkan Mengisi Form untuk Menambahkan Grup Kerja",
            'banner': 'about/img/banner.png',
            'app_css': 'order/css/style.css',
            'form':form4,
        }

        return render(request, 'projectshop/form4.html', context)

def form6(request):
    if request.POST:
        form6 = FormTipeGrup(request.POST)
        if form6.is_valid():
            form6.save()
            form6 = FormTipeGrup()
            pesan = "Tipe Grup Kerja berhasil ditambahkan"
            context = {
                'judul': 'Project Shop SPTM',
                'subjudul': 'Sistem Produksi Terdistribusi Mandiri',
                'heading': "Form Penambahan Asset",
                'subheading': "Silahkan Mengisi Form untuk Menambahkan Tipe Grup Kerja",
                'banner': 'about/img/banner.png',
                'app_css': 'order/css/style.css',
                'form1':form6,
                'pesan' : pesan,
            }
            return render(request, 'projectshop/form6.html', context)

    else:
        form6 = FormTipeGrup()
        context = {
            'judul': 'Project Shop SPTM',
            'subjudul': 'Sistem Produksi Terdistribusi Mandiri',
            'heading': "Form Penambahan Asset",
            'subheading': "Silahkan Mengisi Form untuk Menambahkan Tipe Grup Kerja",
            'banner': 'about/img/banner.png',
            'app_css': 'order/css/style.css',
            'form1':form6,
        }

        return render(request, 'projectshop/form6.html', context)

def form5(request):
    if request.POST:
        form5 = FormProses(request.POST)
        if form5.is_valid():
            form5.save()
            form5 = FormProses()
            pesan = "Proses berhasil ditambahkan"
            context = {
                'judul': 'Project Shop SPTM',
                'subjudul': 'Sistem Produksi Terdistribusi Mandiri',
                'heading': "Form Penambahan Asset",
                'subheading': "Silahkan Mengisi Form untuk Menambahkan Proses",
                'banner': 'about/img/banner.png',
                'app_css': 'order/css/style.css',
                'form':form5,
                'pesan' : pesan,
            }
            return render(request, 'projectshop/form5.html', context)

    else:
        form5 = FormProses()
        context = {
            'judul': 'Project Shop SPTM',
            'subjudul': 'Sistem Produksi Terdistribusi Mandiri',
            'heading': "Form Penambahan Asset",
            'subheading': "Silahkan Mengisi Form untuk Menambahkan Proses",
            'banner': 'about/img/banner.png',
            'app_css': 'order/css/style.css',
            'form':form5,
        }

        return render(request, 'projectshop/form5.html', context)

    # form3 = FormAlat()
    # if request.method == 'POST':
    #     PeralatanKerja.objects.create(
    #         nama_alat = request.POST['nama_alat'],
    #         kodealat_id = request.POST['kodealat_id'],
    #         availabilitas = request.POST['availabilitas'],
    #     )

    # context = {
    #     'judul': 'Project Shop SPTM',
    #     'subjudul': 'Sistem Produksi Terdistribusi Mandiri',
    #     'heading': "Form Penambahan Asset",
    #     'subheading': "Silahkan Mengisi Form untuk Menambahkan Peralatan",
    #     'banner': 'about/img/banner.png',
    #     'app_css': 'order/css/style.css',
    #     'nav': [
    #         ['/' ,'Halaman Utama' ],
    #         ['/projectshop/tambah-asset' ,'Tambah Asset' ],
    #         ['/projectshop/tambah-lapak' ,'Tambah Lapak' ],
    #         ['/projectshop/tambah-kodealat' ,'Tambah Kode Alat' ],
    #         ['/projectshop/tambah-peralatan' ,'Tambah Peralatan' ],
    #     ],
    #     'alat':form3,
    # }
    # return render(request, 'projectshop/form3.html', context)





    # if request.POST:
    #     form = FormLapak(request.POST)
    #     form2 = FormKode(request.POST)
    #     form3 = FormAlat(request.POST)
    #     if  form.is_valid():
    #         form.save()
    #         form = FormLapak()
    #         pesan = "Lapak berhasil ditambahkan"
    #         context = {
    #             'judul': 'Project Shop SPTM',
    #             'subjudul': 'Sistem Produksi Terdistribusi Mandiri',
    #             'heading': "Form Penambahan Asset",
    #             'subheading': "Silahkan Mengisi Form untuk Menambahkan Asset",
    #             'banner': 'about/img/banner.png',
    #             'app_css': 'order/css/style.css',
    #             'nav': [
    #                 ['/' ,'Halaman Utama' ],
    #                 ['/order' ,'Penjadwalan Produksi' ],
    #                 ['/produk' ,'List Produksi' ],
    #                 ['/projectshop' ,'List Asset' ],
    #                 ['/projectshop/tambah-asset' ,'Tambah Asset' ],
    #             ],
    #             'lapak':form,
    #             'kode':form2,
    #             'alat':form3,
    #             'pesan' : pesan,
    #                 }
    #         return render(request, 'projectshop/form.html', context)
    #     elif form2.is_valid():
    #          form2.save()
    #          form2 = FormKode()
    #          pesan = "Kode Alat berhasil ditambahkan"
    #          context = {
    #             'judul': 'Project Shop SPTM',
    #             'subjudul': 'Sistem Produksi Terdistribusi Mandiri',
    #             'heading': "Form Penambahan Asset",
    #             'subheading': "Silahkan Mengisi Form untuk Menambahkan Asset",
    #             'banner': 'about/img/banner.png',
    #             'app_css': 'order/css/style.css',
    #             'nav': [
    #                 ['/' ,'Halaman Utama' ],
    #                 ['/order' ,'Penjadwalan Produksi' ],
    #                 ['/produk' ,'List Produksi' ],
    #                 ['/projectshop' ,'List Asset' ],
    #                 ['/projectshop/tambah-asset' ,'Tambah Asset' ],
    #             ],
    #             'lapak':form,
    #             'kode':form2,
    #             'alat':form3,
    #             'pesan' : pesan,
    #                 }
    #          return render(request, 'projectshop/form.html', context)
    #     elif form3.is_valid():
    #          form3.save()
    #          form3 = FormAlat()
    #          pesan = "Alat berhasil ditambahkan"
    #          context = {
    #             'judul': 'Project Shop SPTM',
    #             'subjudul': 'Sistem Produksi Terdistribusi Mandiri',
    #             'heading': "Form Penambahan Asset",
    #             'subheading': "Silahkan Mengisi Form untuk Menambahkan Asset",
    #             'banner': 'about/img/banner.png',
    #             'app_css': 'order/css/style.css',
    #             'nav': [
    #                 ['/' ,'Halaman Utama' ],
    #                 ['/order' ,'Penjadwalan Produksi' ],
    #                 ['/produk' ,'List Produksi' ],
    #                 ['/projectshop' ,'List Asset' ],
    #                 ['/projectshop/tambah-asset' ,'Tambah Asset' ],
    #             ],
    #             'lapak':form,
    #             'kode':form2,
    #             'alat':form3,
    #             'pesan' : pesan,
    #                 }
    #          return render(request, 'projectshop/form.html', context)

    # else:
    #     form = FormLapak()
    #     form2 = FormKode()
    #     form3 = FormAlat()
    #     context = {
    #         'judul': 'Project Shop SPTM',
    #         'subjudul': 'Sistem Produksi Terdistribusi Mandiri',
    #         'heading': "Form Penambahan Asset",
    #         'subheading': "Silahkan Mengisi Form untuk Menambahkan Asset",
    #         'banner': 'about/img/banner.png',
    #         'app_css': 'order/css/style.css',
    #         'nav': [
    #             ['/' ,'Halaman Utama' ],
    #             ['/order' ,'Penjadwalan Produksi' ],
    #             ['/produk' ,'List Produksi' ],
    #             ['/projectshop' ,'List Asset' ],
    #             ['/projectshop/tambah-asset' ,'Tambah Asset' ],
    #         ],
    #         'lapak':form,
    #         'kode':form2,
    #         'alat':form3,
    #     }

    #     return render(request, 'projectshop/form.html', context)