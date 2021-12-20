# views engineering order

from models.engineeringorder.models import EngineeringOrder
from django.shortcuts import render
from forms.engineeringorder.forms import FormEngineeringOrder

# Create your views here.

def list(request):
    list = EngineeringOrder.objects.all()
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
        'List':list,
    }

    return render(request, 'listengineeringorder.html', context)

def form(request):
    if request.POST:
        form = FormEngineeringOrder(request.POST)
        if form.is_valid():
            form.save()
            form = FormEngineeringOrder()
            pesan = "Engineering Order berhasil didaftarkan"
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
                'form':form,
                'pesan':pesan,
            }

            return render(request, 'formengineeringorder.html', context)

    else:
        form = FormEngineeringOrder()
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
            'form':form,
        }

        return render(request, 'formengineeringorder.html', context)

