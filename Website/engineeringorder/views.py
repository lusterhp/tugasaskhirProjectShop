
# Create your views here.

# views engineering order

from engineeringorder.models import EngineeringOrder, MaterialEO
from django.shortcuts import redirect, render
from django.contrib import messages
from engineeringorder.forms import *
from design.forms import FormMaterialEO
from design.models import *

def detail_list(request, dlid):
    list = EngineeringOrder.objects.get(id=dlid)
    context = {
        'judul': "Project Shop SPTM",
        'subjudul': "Sistem Produksi Terdistribusi Mandiri",
        'heading': "List Detail Engineering Order",
        'subheading': "Berikut Adalah List Detail Engineering Order yang Telah Terdaftar",
        'banner': 'order/img/banner.png',
        'app_css': 'order/css/style.css',
        'nav': [
            ['/engineeringorder' ,'Kembali' ],
        ],
        'list':list,
    }

    return render(request, 'detail-list.html', context)

def list(request):
    list = EngineeringOrder.objects.all()
    list2 = MaterialEO.objects.all()
    mylist = zip(list, list2)
    context = {
        'judul': "Project Shop SPTM",
        'subjudul': "Sistem Produksi Terdistribusi Mandiri",
        'heading': "List Engineering Order",
        'subheading': "Berikut Adalah List Engineering Order yang Telah Terdaftar",
        'banner': 'order/img/banner.png',
        'app_css': 'order/css/style.css',
        'nav': [
            ['/' ,'Halaman Utama' ],
            ['/engineeringorder' ,'List Engineering Order' ],
            ['/engineeringorder/formeo' ,'Form Engineering Order' ],
        ],
        'mylist':mylist,
    }

    return render(request, 'list.html', context)

def delete(request, delete_id):
    EngineeringOrder.objects.filter(id=delete_id).delete()
    return redirect('listeo')

def update1(request, update1_id):
    produk_update1 = EngineeringOrder.objects.get(id=update1_id)
    template = 'ubah-eo.html'
    if request.POST:
        form = FormEngineeringOrder1(request.POST, instance=produk_update1)
        if form.is_valid:
            form.save()
            messages.success(request, "Data berhasil diperbaharui!")
            return redirect(update1, update1_id=update1_id)
    else:
        form = FormEngineeringOrder1(instance=produk_update1)
        konteks = {
            'judul': "Project Shop SPTM",
            'subjudul': "Sistem Produksi Terdistribusi Mandiri",
            'heading': "Form Pembaharuan Engineering Order",
            'subheading': "Berikut Adalah Form Pembaharuan Engineering Order",
            'banner': 'order/img/banner.png',
            'app_css': 'order/css/style.css',
            'form':form,
            'produk':produk_update1,
        }
    return render(request, template, konteks)

def update2(request, update2_id):
    produk_update2 = MaterialEO.objects.get(id=update2_id)
    template = 'ubah-materialeo.html'
    if request.POST:
        form = FormMaterialEO(request.POST, instance=produk_update2)
        if form.is_valid:
            form.save()
            messages.success(request, "Data berhasil diperbaharui!")
            return redirect(update2, update2_id=update2_id)
    else:
        form = FormMaterialEO(instance=produk_update2)
        konteks = {
            'judul': "Project Shop SPTM",
            'subjudul': "Sistem Produksi Terdistribusi Mandiri",
            'heading': "Form Pembaharuan Material Engineering Order",
            'subheading': "Berikut Adalah Form Pembaharuan Material Engineering Order",
            'banner': 'order/img/banner.png',
            'app_css': 'order/css/style.css',
            'form':form,
            'produk':produk_update2,
        }
    return render(request, template, konteks)

def update3(request, update3_id):
    produk_update3 = EngineeringOrder.objects.get(id=update3_id)
    template = 'ubah-persetujuan.html'
    if request.POST:
        form = FormEngineeringOrder2(request.POST, instance=produk_update3)
        if form.is_valid:
            fd = form.save()
            fmeo = MaterialEO.objects.get(penggantiMaterial=fd.material_id)
            gm = Material.objects.filter(id=fmeo.penggantiMaterial.id)
            Material.objects.filter(id=fmeo.penggantiMaterial.id).update(is_berlaku=False)
            mg = Material.objects.create(varian_id = fmeo.varian_id, id_material = fmeo.id_materialeo, nama_material = fmeo.nama_material, nama_supplier = fmeo.nama_supplier, penyusun_produk = fmeo.penyusun_produk, tanggal_berlaku = fmeo.tanggal_berlaku, penggantiMaterial = fmeo.penggantiMaterial)
            Proses.objects.filter(material_id = gm).update(material_id = mg)
            messages.success(request, "Data berhasil diperbaharui!")
            return redirect(update3, update3_id=update3_id)
    else:
        form = FormEngineeringOrder2(instance=produk_update3)
        konteks = {
            'judul': "Project Shop SPTM",
            'subjudul': "Sistem Produksi Terdistribusi Mandiri",
            'heading': "Form Pembaharuan Persetujuan Engineering Order",
            'subheading': "Berikut Adalah Form Pembaharuan Persetujuan Engineering Order",
            'banner': 'order/img/banner.png',
            'app_css': 'order/css/style.css',
            'form':form,
            'produk':produk_update3,
        }
    return render(request, template, konteks)

def form(request):
    if request.POST:
        form = FormEngineeringOrder(request.POST)
        form1 = FormMaterialEO(request.POST)
        if form.is_valid():
            fm = form.save()
            fmeo = form1.save()
            EngineeringOrder.objects.filter(id=fm.id).update(material_id=fmeo.pengganti_material)
            form = FormEngineeringOrder()
            form1 = FormMaterialEO()
            pesan = "Engineering Order berhasil didaftarkan"

            context = {
                'judul': "Project Shop SPTM",
                'subjudul': "Sistem Produksi Terdistribusi Mandiri",
                'heading': "Form Engineering Order",
                'subheading': "Berikut Adalah Form Engineering Order",
                'banner': 'order/img/banner.png',
                'app_css': 'order/css/style.css',
                'form':form,
                'form1':form1,
                'pesan':pesan,
            }

            return render(request, 'form.html', context)

    else:
        form = FormEngineeringOrder()
        form1 = FormMaterialEO()
        context = {
            'judul': "Project Shop SPTM",
            'subjudul': "Sistem Produksi Terdistribusi Mandiri",
            'heading': "Form Engineering Order",
            'subheading': "Berikut Adalah Form Engineering Order",
            'banner': 'order/img/banner.png',
            'app_css': 'order/css/style.css',
            'nav': [
                ['/' ,'Halaman Utama' ],
                ['/engineeringorder' ,'List Engineering Order' ],
                ['/engineeringorder/formeo' ,'Form Engineering Order' ],
            ],
            'form':form,
            'form1':form1,
        }

        return render(request, 'form.html', context)

