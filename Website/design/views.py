
# Create your views here.

# views design

from django.http import HttpResponse
from django.http.response import HttpResponseRedirect, HttpResponseRedirect
from django.conf.urls import url
from django.db.models import Count, Q
from TA import urls
from design.models import *
from django.contrib import messages
from django.shortcuts import redirect, render
from design.forms import *
import datetime

def list(request, idVarianInput):
    bom = Material.objects.filter(varian_id = idVarianInput).filter(is_berlaku=True)
    #bom = Material.objects.filter(varian_id = idVarianInput).filter((Q(tanggalGanti__gt=datetime.datetime.today()) & Q(tanggal_berlaku__lte=datetime.datetime.today()))|(Q(tanggalGanti__isnull=True) & Q(tanggal_berlaku__lte=datetime.datetime.today())))
    bom2 = Proses.objects.filter(varian_id = idVarianInput).order_by('id_proses')
    context = {
        'judul': "Project Shop SPTM",
        'subjudul': "Sistem Produksi Terdistribusi Mandiri",
        'heading': "Struktur Produk dan Model Proses",
        'subheading': "Berikut Adalah Struktur Produk dan Model Proses yang Telah Terdaftar",
        'banner': 'order/img/banner.png',
        'app_css': 'order/css/style.css',    
        'bom':bom,
        'bom2':bom2,    
    }

    return render(request, 'listbom.html', context)

def list1(request):
    list2 = Material.objects.all()
    context = {
        'judul': "Project Shop SPTM",
        'subjudul': "Sistem Produksi Terdistribusi Mandiri",
        'heading': "List Proses Kerja dan Material",
        'subheading': "Berikut Adalah List Proses Kerja dan Material yang Telah Terdaftar",
        'banner': 'order/img/banner.png',
        'app_css': 'order/css/style.css',
        'nav': [
            ['/' ,'Halaman Utama' ],
            ['/design' ,'List Design' ],
            ['/design/formpk' ,'Form Proses Kerja' ],
            ['/design/formmaterial' ,'Form Material' ],
        ],
        'List2':list2,
    }

    return render(request, 'listdesign.html', context)

def delete2(request, hapus_id):
    Material.objects.filter(id=hapus_id).delete()
    return redirect('listproduk')

def deleteproses(request, hapusproses_id):
    Proses.objects.filter(id=hapusproses_id).delete()
    return redirect('listproduk')

def update2(request, update2_id):
    produk_update2 = Material.objects.get(id=update2_id)
    if request.POST:
        form = FormMaterial(request.POST, instance=produk_update2)
        if form.is_valid:
            form.save()
            messages.success(request, "Data berhasil diperbaharui!")
            return redirect(update2, update2_id=update2_id)
    else:
        form = FormMaterial(instance=produk_update2)
        konteks = {
            'judul': "Project Shop SPTM",
            'subjudul': "Sistem Produksi Terdistribusi Mandiri",
            'heading': "Form Pembaharuan Material",
            'subheading': "Berikut Adalah Form Pembaharuan Material",
            'banner': 'order/img/banner.png',
            'app_css': 'order/css/style.css',
            'form':form,
            'produk':produk_update2,
        }
    return render(request, 'ubah-material.html', konteks)

def updateMaterial(request, update_id):
    #cara edit
    material_update = Material.objects.get(id=update_id)

    data = {
        'varian_id': material_update.varian_id,
        'id_material': material_update.id_material,
        'nama_material': material_update.nama_material,
        'nama_supplier': material_update.nama_supplier,
        'penyusun_produk': material_update.penyusun_produk,
        'tanggal_berlaku':material_update.tanggal_berlaku,
    }
    material_form = FormMaterial(request.POST or None, initial=data, instance=material_update)


    if request.method == 'POST':
        # validasi data
        if material_form.is_valid():
            # menyimpan ke database
            material_form.save()
            
        
        return redirect('homeproduk')

    context = {
        'judul': "Project Shop SPTM",
        'subjudul': "Sistem Produksi Terdistribusi Mandiri",
        'heading': "Form Pembaharuan Material",
        'subheading': "Berikut Adalah Form Pendaftaran Material",
        'banner': 'order/img/banner.png',
        'app_css': 'order/css/style.css',
        'form2':material_form,
        'produk':material_update,
    }

    return render(request, 'form3.html', context)

def form(request):
    if request.POST:
        form = FormProses(request.POST)
        if form.is_valid():
            form.save()
            form = FormProses()
            pesan = "Proses berhasil didaftarkan"
            context = {
                'judul': "Project Shop SPTM",
                'subjudul': "Sistem Produksi Terdistribusi Mandiri",
                'heading': "Form Pendaftaran Proses",
                'subheading': "Berikut Adalah Form Pendaftaran Proses",
                'banner': 'order/img/banner.png',
                'app_css': 'order/css/style.css',
                'form2':form,
                'pesan':pesan,
            }

            return render(request, 'formproses.html', context)

    else:
        form = FormProses()
        context = {
            'judul': "Project Shop SPTM",
            'subjudul': "Sistem Produksi Terdistribusi Mandiri",
            'heading': "Form Pendaftaran Proses",
            'subheading': "Berikut Adalah Form Pendaftaran Proses",
            'banner': 'order/img/banner.png',
            'app_css': 'order/css/style.css',
            'form2':form,
        }

        return render(request, 'formproses.html', context)

def form2(request):
    if request.POST:
        form2 = FormMaterial(request.POST)
        if form2.is_valid():
            form2.save()
            form2 = FormMaterial()
            pesan = "Material berhasil didaftarkan"
            context = {
                'judul': "Project Shop SPTM",
                'subjudul': "Sistem Produksi Terdistribusi Mandiri",
                'heading': "Form Pendaftaran Material",
                'subheading': "Berikut Adalah Form Pendaftaran Material",
                'banner': 'order/img/banner.png',
                'app_css': 'order/css/style.css',
                'form2':form2,
                'pesan':pesan,
            }

            return render(request, 'form2.html', context)

    else:
        form2 = FormMaterial()
        context = {
            'judul': "Project Shop SPTM",
            'subjudul': "Sistem Produksi Terdistribusi Mandiri",
            'heading': "Form Pendaftaran Material",
            'subheading': "Berikut Adalah Form Pendaftaran Material",
            'banner': 'order/img/banner.png',
            'app_css': 'order/css/style.css',
            'form2':form2,
        }

        return render(request, 'form2.html', context)

