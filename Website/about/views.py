# views about

from django.shortcuts import render

# Create your views here.

def about(request):
    context = {
        'judul': 'Project Shop SPTM',
        'subjudul': 'Sistem Produksi Terdistribusi Mandiri',
        'heading': "Tentang Pembuat",
        'subheading': "Luster Hiroshi Pramushinto",
        'banner': 'about/img/banner.png',
        'app_css': 'about/css/style.css',
        'nav': [
            ['/' ,'Halaman Utama' ],
            ['/about' ,'Tentang Pembuat' ],
        ],
    }

    return render(request, 'about/about.html', context)
