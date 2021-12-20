from django.shortcuts import render
from order.models import *
import pandas as pd 
import plotly.express as px
from plotly.offline import download_plotlyjs, plot
import plotly.figure_factory as ff
from produk.models import ProdukDijadwalkan

def jadwaloperasi(request, idpd):
    op = Operasi.objects.filter(produkdijadwalkan_id = idpd)
    jop = Operasi.objects.filter(produkdijadwalkan_id = idpd).count()
    pdi = ProdukDijadwalkan.objects.filter(id=idpd)

    task = []
    start = []
    finish = []
    resource = []


    i = 0
    while i <= jop:
        if i == jop:
            break
        if i == 0:
            task.append(op[i].proses_id.nama_proses)
            dumvar = str(op[i].waktu_mulai)
            start.append(dumvar)
            dumvar2 = str(op[i].waktu_selesai)
            finish.append(dumvar2)
            resource.append(op[i].grup_id)
        else:
            task.append(op[i].proses_id.nama_proses)
            dumvar = str(op[i].waktu_mulai)
            start.append(dumvar)
            dumvar2 = str(op[i].waktu_selesai)
            finish.append(dumvar2)
            resource.append(op[i].grup_id)
        i += 1

    data = {'Pekerjaan': task,
	'Mulai': start,
	'Selesai': finish,
	'Grup Kerja': resource}

    df_marks = pd.DataFrame(data)

    fig = px.timeline(df_marks, x_start="Mulai", x_end="Selesai", y="Pekerjaan", color="Grup Kerja")
    fig.update_yaxes(autorange="reversed")
    plot = fig.show()

    context = {
    'judul': "Project Shop SPTM",
    'subjudul': "Sistem Produksi Terdistribusi Mandiri",
    'heading': "Jadwal Operasi",
    'subheading': "Berikut Adalah Jadwal Operasi dari Pesanan",
    'banner': 'order/img/banner.png',
    'app_css': 'order/css/style.css',    
    'fig':plot,
    'operasi': op,
}

    return render(request, 'produk/plot.html', context)

"""
    j = 0 
    while j <= jop:
        if j == jop:
            break
        if j == 0:


    df = pd.DataFrame([

        j = 0
        while j <= jop:
            if j == jop:

        dict(Task=task, Start=start, Finish=finish, Resource=resource),
    ])

    fig = px.timeline(df, x_start="Start", x_end="Finish", y="Task", color="Resource")
    fig.update_yaxes(autorange="reversed")
    plot = fig.show()

    context = {
    'judul': "Project Shop SPTM",
    'subjudul': "Sistem Produksi Terdistribusi Mandiri",
    'heading': "Jadwal Operasi",
    'subheading': "Berikut Adalah Jadwal Operasi dari Pesanan" + pdi.nama_pesanan,
    'banner': 'order/img/banner.png',
    'app_css': 'order/css/style.css',    
    'fig':plot,
    'operasi': op,
}

    return render(request, 'produk/plot.html', context)



    chart.append(
        px.timeline(x_start=start, x_end=finish, y=task, color=resource)
    )
"""