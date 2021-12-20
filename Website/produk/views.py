# views produk

from django.shortcuts import render, redirect
from django.contrib import messages
from order.models import Operasi
from projectshop.models import *
from design.models import *
from .models import *
from .forms import *
import datetime
from datetime import datetime
from datetime import date
import datetime
import time

# Create your views here.



def penjadwalanoperasi(request):
    form1 = FormProdukDijadwalkan(request.POST or None)

    if request.method == 'POST':
        if form1.is_valid():
            pd = form1.save()
            messages.success(request, "Penjadwalan berhasil dibuat!")

            tambah_sejam = datetime.timedelta(hours=1)
            sekarang = datetime.datetime.now()
            hari_ini = date.today()
            jam_sembilan = datetime.time(9,0,0)
            hijs = datetime.datetime.combine(hari_ini,jam_sembilan)
            jam_sebelas = datetime.time(11,0,0)
            hijsebelas = datetime.datetime.combine(hari_ini,jam_sebelas)
            jam_db = datetime.time(12,0,0)
            hijdb = datetime.datetime.combine(hari_ini,jam_db)
            jam_5sore = datetime.time(17,0,0)
            hij5sore = datetime.datetime.combine(hari_ini,jam_5sore)
            hpd = ProdukDijadwalkan.objects.get(id=pd.id)
            pr = Proses.objects.filter(varian_id=hpd.produk_id).order_by('tahapan_pengerjaan' , 'grup_id')
            jumlahpr = Proses.objects.filter(varian_id=hpd.produk_id).count()
            l = LapakKerja.objects.filter(aktif_bekerja=False).count()
            if l != 0:
                ls = LapakKerja.objects.filter(aktif_bekerja=False)[:1]
                ProdukDijadwalkan.objects.filter(id=pd.id).update(lapak_id=ls[0].id)
                #LapakKerja.objects.filter(kode_lapak=ls[0].kode_lapak).update(jadwal_lapak=pd.deadline_diminta)
                
                buat_gp = ProdukDijadwalkan.objects.get(id=pd.id)
                lapak_buatgp = LapakKerja.objects.get(id=buat_gp.lapak_id.id)
                gp = lapak_buatgp.grup_kerja.all()
                print(pr)
                print(jumlahpr)
                print(type(jumlahpr))
                i=0
                j = 0
                while j <= jumlahpr:
                    if j == jumlahpr:
                        ops = Operasi.objects.filter(produkdijadwalkan_id=hpd).order_by('-waktu_selesai')
                        LapakKerja.objects.filter(kode_lapak=ls[0].kode_lapak).update(jadwal_lapak=ops[0].waktu_selesai)
                        break
                    if j == 0:
                        ab = GrupKerja.objects.get(lapakkerja__id=lapak_buatgp.id, kode_grup=pr[j].grup_id)
                        durasi1 = pr[j].durasi
                        print(durasi1)
                        durasi1_int = int(durasi1)
                        jam1 = durasi1_int//60
                        print(jam1)
                        menit1 = durasi1_int %60
                        print(menit1)
                        detik1 = (durasi1_int*60) %60
                        print(detik1)
                        timedelta1 = datetime.timedelta(hours=jam1, minutes=menit1, seconds=detik1)
                        print(timedelta1)
                        ws = sekarang + timedelta1
                        print(ab)
                        if sekarang < hijs:
                            ws1 = hijs + timedelta1
                            print('sebelum if keempat')
                            if (ws1 > hijsebelas) and (ws1 <= hij5sore):
                                ws1_1 = ws1 + tambah_sejam
                                Operasi.objects.create(produkdijadwalkan_id = hpd, proses_id = pr[j], grup_id=ab, waktu_mulai = hijs, waktu_selesai=ws1_1)
                                print('Berhasil')
                            elif ws1 > hij5sore:
                                tambah_banget = datetime.timedelta(hours=17)
                                ws1_2 = ws1 + tambah_banget
                                Operasi.objects.create(produkdijadwalkan_id = hpd, proses_id = pr[j], grup_id=ab,waktu_mulai = hijs, waktu_selesai=ws1_2)
                                print('Berhasil')
                            else:
                                Operasi.objects.create(produkdijadwalkan_id = hpd, proses_id = pr[j], grup_id=ab,waktu_mulai = hijs, waktu_selesai=ws1)
                                print('Berhasil')
                        elif (sekarang >= hijsebelas) and (sekarang < hijdb):
                            ws2 = sekarang + timedelta1 + tambah_sejam
                            if ws2 > hij5sore:
                                tambah_banget2 = datetime.timedelta(hours=17)
                                ws2_1 = sekarang + tambah_banget2
                                Operasi.objects.create(produkdijadwalkan_id = hpd, proses_id = pr[j], grup_id=ab,waktu_mulai = sekarang, waktu_selesai=ws2_1)
                                print('Berhasil')
                            else:
                                Operasi.objects.create(produkdijadwalkan_id = hpd, proses_id = pr[j], grup_id=ab,waktu_mulai = sekarang, waktu_selesai=ws2)
                                print('Berhasil')
                        elif sekarang >= hij5sore:
                            tambah_hari = datetime.timedelta(hours=24)
                            bjs = hijs + tambah_hari
                            ws3 = bjs + timedelta1
                            bjsebelas = hijsebelas + tambah_hari
                            bj5sore = hij5sore + tambah_hari
                            if ws3 > bjsebelas:
                                ws3_1 = ws3 + tambah_sejam
                                Operasi.objects.create(produkdijadwalkan_id = hpd, proses_id = pr[j], grup_id=ab,waktu_mulai = bjs, waktu_selesai=ws3_1)
                                print('Berhasil')
                            elif ws3 > bj5sore:
                                tambah_banget3 = datetime.timedelta(hours=17)
                                ws3_2 = ws3 + tambah_banget3
                                Operasi.objects.create(produkdijadwalkan_id = hpd, proses_id = pr[j], grup_id=ab,waktu_mulai = bjs, waktu_selesai=ws3_2)
                                print('Berhasil')
                            else:
                                Operasi.objects.create(produkdijadwalkan_id = hpd, proses_id = pr[j], grup_id=ab,waktu_mulai = bjs, waktu_selesai=ws3)
                                print('Berhasil')
                        else:
                            Operasi.objects.create(produkdijadwalkan_id = hpd, proses_id = pr[j], grup_id=ab,waktu_mulai = sekarang, waktu_selesai=ws)
                            print('Berhasil')
                    else:
                        ab = GrupKerja.objects.get(lapakkerja__id=lapak_buatgp.id, kode_grup=pr[j].grup_id)
                        durasi = pr[j].durasi
                        tg = pr[j].grup_id
                        wm = Operasi.objects.filter(produkdijadwalkan_id=hpd)
                        if i == jumlahpr:
                            break
                        else:
                            print(ab)
                            print('i adalah', i)
                            print(pr[j])
                            print(pr[j].grup_id)
                            wmo = wm[i].waktu_selesai
                            #wm_o = str(wmo)
                            #FMT = '%Y-%m-%d %H:%M:%S'
                            durasi_int = int(durasi)
                            jam = durasi_int//60
                            menit = durasi_int %60
                            detik = (durasi_int*60) %60
                            timedelta = datetime.timedelta(hours=jam, minutes=menit, seconds=detik)
                            #wm_fix = datetime.datetime.strptime(wm_o, FMT)
                            wm_tanggal = datetime.datetime(wmo.year, wmo.month, wmo.day)
                            wm_waktu = datetime.time(wmo.hour, wmo.minute, wmo.second)
                            wm_fix = datetime.datetime.combine(wm_tanggal, wm_waktu)
                            js = datetime.datetime.combine(wm_tanggal,jam_sembilan)
                            print(wm_fix)
                            print(js)
                            jsebelas = datetime.datetime.combine(wm_tanggal,jam_sebelas)
                            j5sore = datetime.datetime.combine(wm_tanggal,jam_5sore)
                            jdb = datetime.datetime.combine(wm_tanggal,jam_db)
                            ws4 = wm_fix + timedelta
                            if wm_fix < js:
                                ws5 = js + timedelta
                                if (ws5 > jsebelas) and (ws5 <= j5sore):
                                    ws5_1 = ws5 + tambah_sejam
                                    Operasi.objects.create(produkdijadwalkan_id = hpd, proses_id = pr[j], grup_id=ab,waktu_mulai = js, waktu_selesai=ws5_1)
                                    print('Berhasil')
                                    i +=1
                                elif ws5 > j5sore:
                                    tambah_banget4 = datetime.timedelta(hours=17)
                                    ws5_2 = ws5 + tambah_banget4
                                    Operasi.objects.create(produkdijadwalkan_id = hpd, proses_id = pr[j], grup_id=ab,waktu_mulai = js, waktu_selesai=ws5_2)
                                    print('Berhasil')
                                    i +=1
                                else:
                                    Operasi.objects.create(produkdijadwalkan_id = hpd, proses_id = pr[j], grup_id=ab,waktu_mulai = js, waktu_selesai=ws5)
                                    print('Berhasil')
                                    i +=1
                            elif (wm_fix >= jsebelas) and (wm_fix < jdb):
                                ws6 = sekarang + timedelta + tambah_sejam
                                if ws6 > j5sore:
                                    tambah_banget5 = datetime.timedelta(hours=17)
                                    ws6_1 = sekarang + tambah_banget5
                                    Operasi.objects.create(produkdijadwalkan_id = hpd, proses_id = pr[j], grup_id=ab,waktu_mulai = wm_fix, waktu_selesai=ws6_1)
                                    print('Berhasil')
                                    i +=1
                                else:
                                    Operasi.objects.create(produkdijadwalkan_id = hpd, proses_id = pr[j], grup_id=ab,waktu_mulai = wm_fix, waktu_selesai=ws6)
                                    print('Berhasil')
                                    i +=1
                            elif wm_fix >= j5sore:
                                tambah_hari = datetime.timedelta(hours=24)
                                jsb = js + tambah_hari
                                ws7 = jsb + timedelta
                                bjsebelas = jsebelas + tambah_hari
                                bj5sore = j5sore + tambah_hari
                                if ws7 > bjsebelas:
                                    ws7_1 = ws7 + tambah_sejam
                                    Operasi.objects.create(produkdijadwalkan_id = hpd, proses_id = pr[j], grup_id=ab,waktu_mulai = jsb, waktu_selesai=ws7_1)
                                    print('Berhasil')
                                    i +=1
                                elif ws7 > bj5sore:
                                    tambah_banget6 = datetime.timedelta(hours=17)
                                    ws7_2 = ws7 + tambah_banget6
                                    Operasi.objects.create(produkdijadwalkan_id = hpd, proses_id = pr[j], grup_id=ab,waktu_mulai = jsb, waktu_selesai=ws7_2)
                                    print('Berhasil')
                                    i +=1
                                else:
                                    Operasi.objects.create(produkdijadwalkan_id = hpd, proses_id = pr[j], grup_id=ab,waktu_mulai = jsb, waktu_selesai=ws7)
                                    print('Berhasil')
                                    i +=1
                            else:
                                Operasi.objects.create(produkdijadwalkan_id = hpd, proses_id = pr[j], grup_id=ab, waktu_mulai = wm_fix, waktu_selesai=ws4)
                                print('Berhasil')
                                i +=1
                    j +=1
            elif l == 0:
                lb = LapakKerja.objects.filter(aktif_bekerja=True).order_by('jadwal_lapak')[:1]
                wmo1 = lb[0].jadwal_lapak
                ProdukDijadwalkan.objects.filter(id=pd.id).update(lapak_id=lb[0].id)
                #LapakKerja.objects.filter(kode_lapak=lb[0].kode_lapak).update(jadwal_lapak=pd.deadline_diminta)
                
                buat_gp = ProdukDijadwalkan.objects.get(id=pd.id)
                lapak_buatgp = LapakKerja.objects.get(id=buat_gp.lapak_id.id)
                gp = lapak_buatgp.grup_kerja.all()
                i=0
                j = 0
                while j <= jumlahpr:
                    if j == jumlahpr:
                        ops1 = Operasi.objects.filter(produkdijadwalkan_id = hpd).order_by('-waktu_selesai')
                        LapakKerja.objects.filter(kode_lapak=lb[0].kode_lapak).update(jadwal_lapak=ops1[0].waktu_selesai)
                        break
                    if j == 0:
                        ab = GrupKerja.objects.get(lapakkerja__id=lapak_buatgp.id, kode_grup=pr[j].grup_id)
                        #wm_o1 = str(wmo1)
                        #FMT = '%Y-%m-%d %I:%M:%S %p'
                        durasi2 = pr[j].durasi
                        durasi2_int = int(durasi2)
                        jam2 = durasi2_int // 60
                        menit2 = durasi2_int %60
                        detik2 = (durasi2_int*60) %60
                        timedelta2 = datetime.timedelta(hours=jam2, minutes=menit2, seconds=detik2)
                        #wm_fix1 = datetime.datetime.strptime(wm_o1, FMT)
                        wm_tanggal1 = datetime.datetime(wmo1.year, wmo1.month, wmo1.day)
                        wm_waktu1 = datetime.time(wmo1.hour, wmo1.minute, wmo1.second)
                        wm_fix1 = datetime.datetime.combine(wm_tanggal1, wm_waktu1)
                        js1 = datetime.datetime.combine(wm_tanggal1,jam_sembilan)
                        jsebelas1 = datetime.datetime.combine(wm_tanggal1,jam_sebelas)
                        j5sore1 = datetime.datetime.combine(wm_tanggal1,jam_5sore)
                        jdb1 = datetime.datetime.combine(wm_tanggal1,jam_db)
                        ws8 = wm_fix1 + timedelta2
                        if wm_fix1 < js1:
                            ws9 = js1 + timedelta2
                            if (ws9 > jsebelas1) and (ws9 <= j5sore1):
                                ws9_1 = ws9 + tambah_sejam
                                Operasi.objects.create(produkdijadwalkan_id = hpd, proses_id = pr[j], grup_id=ab, waktu_mulai = js1, waktu_selesai=ws9_1)
                            elif ws9 > j5sore1:
                                tambah_banget7 = datetime.timedelta(hours=17)
                                ws9_2 = ws9 + tambah_banget7
                                Operasi.objects.create(produkdijadwalkan_id = hpd, proses_id = pr[j], grup_id=ab, waktu_mulai = js1, waktu_selesai=ws9_2)
                            else:
                                Operasi.objects.create(produkdijadwalkan_id = hpd, proses_id = pr[j], grup_id=ab, waktu_mulai = js1, waktu_selesai=ws9)
                        elif (wm_fix1 >= jsebelas1) and (wm_fix1 < jdb1):
                            ws10 = wm_fix1 + timedelta2 + tambah_sejam
                            if ws10 > j5sore1:
                                tambah_banget8 = datetime.timedelta(hours=17)
                                ws10_1 = wm_fix1 + tambah_banget8
                                Operasi.objects.create(produkdijadwalkan_id = hpd, proses_id = pr[j], grup_id=ab, waktu_mulai = wm_fix1, waktu_selesai=ws10_1)
                            else:
                                Operasi.objects.create(produkdijadwalkan_id = hpd, proses_id = pr[j], grup_id=ab, waktu_mulai = wm_fix1, waktu_selesai=ws10)
                        elif wm_fix1 >= j5sore1:
                            tambah_hari = datetime.timedelta(hours=24)
                            bjs = js1 + tambah_hari
                            ws11 = bjs + timedelta2
                            bjsebelas = jsebelas1 + tambah_hari
                            bj5sore = j5sore1 + tambah_hari
                            if ws11 > bjsebelas:
                                ws11_1 = ws11 + tambah_sejam
                                Operasi.objects.create(produkdijadwalkan_id = hpd, proses_id = pr[j], grup_id=ab, waktu_mulai = bjs, waktu_selesai=ws11_1)
                            elif ws11 > bj5sore:
                                tambah_banget9 = datetime.timedelta(hours=17)
                                ws11_2 = ws11 + tambah_banget9
                                Operasi.objects.create(produkdijadwalkan_id = hpd, proses_id = pr[j], grup_id=ab, waktu_mulai = bjs, waktu_selesai=ws11_2)
                            else:
                                Operasi.objects.create(produkdijadwalkan_id = hpd, proses_id = pr[j], grup_id=ab, waktu_mulai = bjs, waktu_selesai=ws11)
                        else:
                            Operasi.objects.create(produkdijadwalkan_id = hpd, proses_id = pr[j], grup_id=ab, waktu_mulai = wm_fix1, waktu_selesai=ws8)
                    else:
                        ab = GrupKerja.objects.get(lapakkerja__id=lapak_buatgp.id, kode_grup=pr[j].grup_id)
                        durasi3 = pr[j].durasi
                        wm3 = Operasi.objects.filter(produkdijadwalkan_id=hpd)
                        if i == jumlahpr:
                            break
                        else:
                            wmo3 = wm3[i].waktu_selesai
                            #wm_o3 = str(wmo3)
                            #FMT = '%Y-%m-%d %I:%M:%S %p'
                            durasi3_int = int(durasi3)
                            jam3 = durasi3_int // 60
                            menit3 = durasi3_int %60
                            detik3 = (durasi3_int*60) %60
                            timedelta3 = datetime.timedelta(hours=jam3, minutes=menit3, seconds=detik3)
                            #wm_fix3 = datetime.datetime.strptime(wm_o3, FMT)
                            wm_tanggal3 = datetime.datetime(wmo3.year, wmo3.month, wmo3.day)
                            wm_waktu3 = datetime.time(wmo3.hour, wmo3.minute, wmo3.second)
                            wm_fix3 = datetime.datetime.combine(wm_tanggal3, wm_waktu3)
                            js3 = datetime.datetime.combine(wm_tanggal3,jam_sembilan)
                            jsebelas3 = datetime.datetime.combine(wm_tanggal3,jam_sebelas)
                            j5sore3 = datetime.datetime.combine(wm_tanggal3,jam_5sore)
                            jdb3 = datetime.datetime.combine(wm_tanggal3,jam_db)
                            ws13 = wm_fix3 + timedelta3
                            if wm_fix3 < js3:
                                ws13 = js3 + timedelta3
                                if (ws13 > jsebelas3) and (ws13 <= j5sore3):
                                    ws13_1 = ws13 + tambah_sejam
                                    Operasi.objects.create(produkdijadwalkan_id = hpd, proses_id = pr[j], grup_id=ab, waktu_mulai = js3, waktu_selesai=ws13_1)
                                    i +=1
                                elif ws13 > j5sore3:
                                    tambah_banget10 = datetime.timedelta(hours=17)
                                    ws13_2 = ws13 + tambah_banget10
                                    Operasi.objects.create(produkdijadwalkan_id = hpd, proses_id = pr[j], grup_id=ab, waktu_mulai = js3, waktu_selesai=ws13_2)
                                    i +=1
                                else:
                                    Operasi.objects.create(produkdijadwalkan_id = hpd, proses_id = pr[j], grup_id=ab, waktu_mulai = js3, waktu_selesai=ws13)
                                    i +=1
                            elif (wm_fix3 >= jsebelas3) and (wm_fix3 < jdb3):
                                ws14 = js3 + timedelta3 + tambah_sejam
                                if ws14 > j5sore3:
                                    tambah_banget11 = datetime.timedelta(hours=17)
                                    ws14_1 = js3 + tambah_banget11
                                    Operasi.objects.create(produkdijadwalkan_id = hpd, proses_id = pr[j], grup_id=ab, waktu_mulai = wm_fix3, waktu_selesai=ws14_1)
                                    i +=1
                                else:
                                    Operasi.objects.create(produkdijadwalkan_id = hpd, proses_id = pr[j], grup_id=ab, waktu_mulai = wm_fix3, waktu_selesai=ws14)
                                    i +=1
                            elif wm_fix3 >= j5sore3:
                                tambah_hari = datetime.timedelta(hours=24)
                                jsb3 = js3 + tambah_hari
                                ws15 = jsb3 + timedelta3
                                bjsebelas3 = jsebelas3 + tambah_hari
                                bj5sore3 = j5sore3 + tambah_hari
                                if ws15 > bjsebelas3:
                                    ws15_1 = ws15 + tambah_sejam
                                    Operasi.objects.create(produkdijadwalkan_id = hpd, proses_id = pr[j], grup_id=ab, waktu_mulai = jsb3, waktu_selesai=ws15_1)
                                    i +=1
                                elif ws15 > bj5sore3:
                                    tambah_banget12 = datetime.timedelta(hours=17)
                                    ws15_2 = ws15 + tambah_banget12
                                    Operasi.objects.create(produkdijadwalkan_id = hpd, proses_id = pr[j], grup_id=ab, waktu_mulai = jsb3, waktu_selesai=ws15_2)
                                    i +=1
                                else:
                                    Operasi.objects.create(produkdijadwalkan_id = hpd, proses_id = pr[j], grup_id=ab, waktu_mulai = jsb3, waktu_selesai=ws15)
                                    i +=1
                            else:
                                Operasi.objects.create(produkdijadwalkan_id = hpd, proses_id = pr[j], grup_id=ab, waktu_mulai = wm_fix3, waktu_selesai=ws13)
                                i +=1
                    j += 1
        
        return redirect('formprodukdijadwalkan')
    context = {
            'judul': 'Project Shop SPTM',
            'subjudul': 'Sistem Produksi Terdistribusi Mandiri',
            'heading': "Form Permintaan Penjadwalan Produk",
            'subheading': "Silahkan Mengisi Form untuk Meminta Penjadwalan Produk",
            'banner': 'about/img/banner.png',
            'app_css': 'order/css/style.css',
            'form':form1,
    }

    return render(request, 'produk/mintajadwal.html', context)


def homeproduk(request):
    context = {
        'judul': 'Project Shop SPTM',
        'subjudul': 'Sistem Produksi Terdistribusi Mandiri',
        'heading': "Produk",
        'subheading': "Silahkan Memilih Salah Satu Tautan Produk",
        'banner': 'about/img/banner.png',
        'app_css': 'order/css/style.css',
    }

    return render(request, 'produk/homeproduk.html', context)

def jadwaloperasi(request):
    context = {
        'judul': 'Project Shop SPTM',
        'subjudul': 'Sistem Produksi Terdistribusi Mandiri',
        'heading': "Jadwal Operasi",
        'subheading': "Berikut merupakan Jadwal Operasi untuk Produk yang dipilih",
        'banner': 'about/img/banner.png',
        'app_css': 'order/css/style.css',
    }

    return render(request, 'produk/jadwaloperasi.html', context)

def tambah(request):
    context = {
        'judul': 'Project Shop SPTM',
        'subjudul': 'Sistem Produksi Terdistribusi Mandiri',
        'heading': "Form Penambahan Produk",
        'subheading': "Silahkan Mengisi Form untuk Menambahkan Produk",
        'banner': 'about/img/banner.png',
        'app_css': 'order/css/style.css',
        'nav': [
            ['/' ,'Halaman Utama' ],
            ['/produk' ,'Katalog Produk' ],
            ['/produk/tambah' ,'Halaman Penambahan Produk' ],
        ],
    }

    return render(request, 'produk/tambah.html', context)

def produk(request):
    form1 = FormProduk(request.POST or None)
    if request.method == 'POST':
        if form1.is_valid():
            form1.save()
            form1 = FormProduk()
            pesan = "Produk Berhasil Ditambahkan"
            context = {
                'judul': 'Project Shop SPTM',
                'subjudul': 'Sistem Produksi Terdistribusi Mandiri',
                'heading': "Form Penambahan Produk",
                'subheading': "Silahkan Mengisi Form untuk Menambahkan Produk",
                'banner': 'about/img/banner.png',
                'app_css': 'order/css/style.css',
                'produk':form1,
                'pesan' : pesan,
            }

            return render(request, 'produk/produk.html', context)
    
    else:
        form1 = FormProduk()
        context = {
            'judul': 'Project Shop SPTM',
            'subjudul': 'Sistem Produksi Terdistribusi Mandiri',
            'heading': "Form Penambahan Produk",
            'subheading': "Silahkan Mengisi Form untuk Menambahkan Produk",
            'banner': 'about/img/banner.png',
            'app_css': 'order/css/style.css',
            'produk':form1,
        }

        return render(request, 'produk/produk.html', context)

def update1(request, update1_id):
    produk_update1 = Produk.objects.get(id=update1_id)
    template = 'produk/ubah-produk.html'
    if request.POST:
        form = FormProduk(request.POST, instance=produk_update1)
        if form.is_valid:
            form.save()
            messages.success(request, "Data berhasil diperbaharui!")
            return redirect(update1, update1_id=update1_id)
    else:
        form = FormProduk(instance=produk_update1)
        konteks = {
            'judul': "Project Shop SPTM",
            'subjudul': "Sistem Produksi Terdistribusi Mandiri",
            'heading': "Form Pembaharuan Model Produk",
            'subheading': "Berikut Adalah Form Pembaharuan Model Produk",
            'banner': 'order/img/banner.png',
            'app_css': 'order/css/style.css',
            'nav': [
                ['/' ,'Halaman Utama' ],
                ['/produk' ,'Katalog Produk' ],
                ['/produk/tambah' ,'Halaman Penambahan Produk' ],
            ],
            'form':form,
            'produk':produk_update1,
        }
    return render(request, template, konteks)

def produk1(request):
    form1 = FormBrand(request.POST or None)
    form2 = FormModel(request.POST or None)
    form3 = FormVariant(request.POST or None)
    if request.method == 'POST':
        if form1.is_valid():
            form1.save()
            form2.save()
            form3.save()
            form1 = FormBrand()
            form2 = FormModel()
            form3 = FormVariant()
            pesan = "Produk berhasil ditambahkan"
            context = {
                'judul': 'Project Shop SPTM',
                'subjudul': 'Sistem Produksi Terdistribusi Mandiri',
                'heading': "Form Penambahan Produk",
                'subheading': "Silahkan Mengisi Form untuk Menambahkan Produk",
                'banner': 'about/img/banner.png',
                'app_css': 'order/css/style.css',
                'produk':form1,
                'model':form2,
                'variant':form3,
                'pesan' : pesan,
            }

            return render(request, 'produk/produk.html', context)

    else:
        form1 = FormBrand()
        form2 = FormModel()
        form3 = FormVariant()
        context = {
            'judul': 'Project Shop SPTM',
            'subjudul': 'Sistem Produksi Terdistribusi Mandiri',
            'heading': "Form Penambahan Produk",
            'subheading': "Silahkan Mengisi Form untuk Menambahkan Produk",
            'banner': 'about/img/banner.png',
            'app_css': 'order/css/style.css',
            'produk':form1,
            'model' : form2,
            'variant':form3,
        }

        return render(request, 'produk/produk.html', context)      

def update3(request, update1_id):
    produk_update1 = Brand.objects.get(id=update1_id)
    produk_update2 = Model.objects.get(id=update1_id)
    produk_update3 = Variant.objects.get(id=update1_id)
    form1 = FormBrand(request.POST or None, instance=produk_update1)
    form2 = FormModel(request.POST or None, instance=produk_update2)
    form3 = FormVariant(request.POST or None, instance=produk_update3)
    template = 'produk/ubah-produk.html'
    if request.method == 'POST':
        if form1.is_valid():
            form1.save()
            form2.save()
            if form3.is_valid():
                form3.save()
                form1 = FormBrand()
                form2 = FormModel()
                form3 = FormVariant()
                messages.success(request, "Data berhasil diperbaharui!")
                return redirect(update1, update1_id=update1_id)
    else:
        form1 = FormBrand(instance=produk_update1)
        form2 = FormModel(instance=produk_update2)
        form3 = FormVariant(instance=produk_update3)
        konteks = {
            'judul': "Project Shop SPTM",
            'subjudul': "Sistem Produksi Terdistribusi Mandiri",
            'heading': "Form Pembaharuan Brand",
            'subheading': "Berikut Adalah Form Pembaharuan Brand",
            'banner': 'order/img/banner.png',
            'app_css': 'order/css/style.css',
            'form1':form1,
            'form2':form2,
            'form3':form3,
            'produk':produk_update1,
        }
    return render(request, template, konteks) 

def model(request):
    if request.POST:
        form2 = FormModel(request.POST)
        if form2.is_valid():
            form2.save()
            form2 = FormModel()
            pesan = "Model Produk berhasil ditambahkan"
            context = {
                'judul': 'Project Shop SPTM',
                'subjudul': 'Sistem Produksi Terdistribusi Mandiri',
                'heading': "Form Penambahan Produk",
                'subheading': "Silahkan Mengisi Form untuk Menambahkan Produk",
                'banner': 'about/img/banner.png',
                'app_css': 'order/css/style.css',
                'nav': [
                    ['/' ,'Halaman Utama' ],
                    ['/produk/tambah' ,'Halaman Penambahan Produk' ],
                    ['/produk/tambah-model' ,'Tambah Model Produk' ],
                ],
                'model':form2,
                'pesan': pesan,
            }

            return render(request, 'produk/model.html', context)

    else:
        form2 = FormModel()
        context = {
            'judul': 'Project Shop SPTM',
            'subjudul': 'Sistem Produksi Terdistribusi Mandiri',
            'heading': "Form Penambahan Produk",
            'subheading': "Silahkan Mengisi Form untuk Menambahkan Produk",
            'banner': 'about/img/banner.png',
            'app_css': 'order/css/style.css',
            'nav': [
                ['/' ,'Halaman Utama' ],
                ['/produk/tambah' ,'Halaman Penambahan Produk' ],
                ['/produk/tambah-model' ,'Tambah Model Produk' ],
            ],
            'model':form2,
        }

        return render(request, 'produk/produk.html', context)

def variant(request):
    template = 'produk/produk.html'
    if request.POST:
        form3 = FormVariant(request.POST)
        if form3.is_valid():
            form3.save()
            form3 = FormVariant()
            pesan = "Produk berhasil ditambahkan"
            context = {
                'judul': 'Project Shop SPTM',
                'subjudul': 'Sistem Produksi Terdistribusi Mandiri',
                'heading': "Form Penambahan Produk",
                'subheading': "Silahkan Mengisi Form untuk Menambahkan Produk",
                'banner': 'about/img/banner.png',
                'app_css': 'order/css/style.css',
                'varian':form3,
                'pesan' : pesan,
            }

            return render(request, template, context)

    else:
        form3 = FormVariant()
        context = {
            'judul': 'Project Shop SPTM',
            'subjudul': 'Sistem Produksi Terdistribusi Mandiri',
            'heading': "Form Penambahan Produk",
            'subheading': "Silahkan Mengisi Form untuk Menambahkan Produk",
            'banner': 'about/img/banner.png',
            'app_css': 'order/css/style.css',
            'varian':form3,
        }

        return render(request, 'produk/produk.html', context)  

def produkdijadwalkan(request):
    if request.POST:
        form = FormProdukDijadwalkan(request.POST)
        if form.is_valid():
            form.save()
            form = FormProdukDijadwalkan()
            pesan = "Produk berhasil diminta penjadwalannya"
            context = {
                'judul': 'Project Shop SPTM',
                'subjudul': 'Sistem Produksi Terdistribusi Mandiri',
                'heading': "Form Permintaan Penjadwalan Produk",
                'subheading': "Silahkan Mengisi Form untuk Meminta Penjadwalan Produk",
                'banner': 'about/img/banner.png',
                'app_css': 'order/css/style.css',
                'minta':form,
                'pesan' : pesan,
            }

            return render(request, 'produk/minta.html', context)

    else:
        form = FormProdukDijadwalkan()
        context = {
            'judul': 'Project Shop SPTM',
            'subjudul': 'Sistem Produksi Terdistribusi Mandiri',
            'heading': "Form Permintaan Penjadwalan Produk",
            'subheading': "Silahkan Mengisi Form untuk Meminta Penjadwalan Produk",
            'banner': 'about/img/banner.png',
            'app_css': 'order/css/style.css',
            'minta':form,
        }

        return render(request, 'produk/minta.html', context)

def list(request):
    list1 = Produk.objects.all()
    context = {
        'judul': 'Project Shop SPTM',
        'subjudul': 'Sistem Produksi Terdistribusi Mandiri',
        'heading': "Katalog Produk",
        'subheading': "Berikut Adalah Katalog Produk yang Telah Dijadwalkan Produksinya",
        'banner': 'about/img/banner.png',
        'app_css': 'order/css/style.css',
        'list1':list1,
    }

    return render(request, 'produk/list.html', context)

def list1(request):
    list1 = Brand.objects.all()
    list2 = Model.objects.all()
    list3 = Variant.objects.all()
    zippedlist = zip(list1, list2, list3)
    context = {
        'judul': 'Project Shop SPTM',
        'subjudul': 'Sistem Produksi Terdistribusi Mandiri',
        'heading': "Katalog Produk",
        'subheading': "Berikut Adalah Katalog Produk yang Telah Dijadwalkan Produksinya",
        'banner': 'about/img/banner.png',
        'app_css': 'order/css/style.css',
        'list1':list1,
        'list2':list2,
        'list3':list3,
        'list' : zippedlist,
    }

    return render(request, 'produk/list.html', context)

def delete1(request, delete1_id):
    Produk.objects.filter(id=delete1_id).delete()
    return redirect('listproduk')

def delete2(request, delete2_id):
    Model.objects.filter(id=delete2_id).delete()
    return redirect('listproduk')

def update2(request, update2_id):
    produk_update2 = Model.objects.get(id=update2_id)
    template = 'produk/ubah-model.html'
    if request.POST:
        form = FormModel(request.POST, instance=produk_update2)
        if form.is_valid:
            form.save()
            messages.success(request, "Data berhasil diperbaharui!")
            return redirect(update2, update2_id=update2_id)
    else:
        form = FormModel(instance=produk_update2)
        konteks = {
            'judul': "Project Shop SPTM",
            'subjudul': "Sistem Produksi Terdistribusi Mandiri",
            'heading': "Form Pembaharuan Model Produk",
            'subheading': "Berikut Adalah Form Pembaharuan Model Produk",
            'banner': 'order/img/banner.png',
            'app_css': 'order/css/style.css',
            'nav': [
                ['/' ,'Halaman Utama' ],
                ['/produk' ,'Katalog Produk' ],
                ['/produk/tambah' ,'Halaman Penambahan Produk' ],
            ],
            'form':form,
            'produk':produk_update2,
        }
    return render(request, template, konteks)

def listprodukdijadwalkan(request):
    home = ProdukDijadwalkan.objects.all()
    home2 = Operasi.objects.filter(produkdijadwalkan_id=home)
    mylist = zip(home, home2)
    template = 'produk/produkdijadwalkan.html'
    context = {
        'judul': 'Project Shop SPTM',
        'subjudul': 'Sistem Produksi Terdistribusi Mandiri',
        'konten': '',
        'banner': 'img/banner.png',
        'home': home,
        'mylist' : mylist,
    }

    return render(request, template, context)

def delete(request, delete_id):
    ProdukDijadwalkan.objects.filter(id=delete_id).delete()
    return redirect('produkdijadwalkan')

def update(request, update_id):
    produkjadwal_update = ProdukDijadwalkan.objects.get(id=update_id)
    template = 'produk/ubah-produk-dijadwalkan.html'
    if request.POST:
        form = FormProdukDijadwalkan(request.POST, instance=produkjadwal_update)
        if form.is_valid:
            form.save()
            messages.success(request, "Data berhasil diperbaharui!")
            return redirect(update, update_id=update_id)
    else:
        form = FormProdukDijadwalkan(instance=produkjadwal_update)
        konteks = {
            'judul': "Project Shop SPTM",
            'subjudul': "Sistem Produksi Terdistribusi Mandiri",
            'heading': "Form Pembaharuan Produk yang Dijadwalkan",
            'subheading': "Berikut Adalah Form Pembaharuan Produk yang Dijadwalkan",
            'banner': 'order/img/banner.png',
            'app_css': 'order/css/style.css',
            'form':form,
            'home':produkjadwal_update,
        }
    return render(request, template, konteks)


#def update1(request, update1_id):
    produkjadwal_update1 = ProdukDijadwalkan.objects.get(id=update1_id)

    data = {
        'status_design' : produkjadwal_update1.status_design,
        'status_operasi' : produkjadwal_update1.status_operasi,
        'variant_id' : produkjadwal_update1.variant_id,
        'jadwal_diminta' : produkjadwal_update1.jadwal_diminta,
    }

    produkdijadwalkan_form = FormProdukDijadwalkan(request.POST or None, initial=data, instance=produkjadwal_update1)

    if request.method=='POST':
        if produkdijadwalkan_form.is_valid():
            produkdijadwalkan_form.save()
            return redirect('home')
            pesan = "Operasi berhasil diperbaharui"
            context = {
                'judul': "Project Shop SPTM",
                'subjudul': "Sistem Produksi Terdistribusi Mandiri",
                'heading': "Form Pembaharuan Operasi",
                'subheading': "Berikut Adalah Form Pembaharuan Operasi",
                'banner': 'order/img/banner.png',
                'app_css': 'order/css/style.css',
                'nav': [
                    ['/' ,'Halaman Utama' ],
                    ['/operasi' ,'List Jadwal Operasi' ],
                    ['/operasi/formoperasi' ,'Form Pendaftaran Operasi' ],
                ],
                'pesan':pesan,
            }
            return redirect('listop') 
    else:
        context = {
            'judul': "Project Shop SPTM",
            'subjudul': "Sistem Produksi Terdistribusi Mandiri",
            'heading': "Form Pembaharuan",
            'subheading': "Berikut Adalah Form Pembaharuan",
            'banner': 'order/img/banner.png',
            'app_css': 'order/css/style.css',
            'nav': [
                ['/' ,'Halaman Utama' ],
                ['/about' ,'Tentang Pembuat' ],
                ['/produk' ,'Katalog Produk' ],
                ['/design' ,'List Design' ],
                ['/operasi' ,'List Jadwal Operasi' ],
                ['/engineeringorder' ,'List Engineering Order' ],
                ['/projectshop' ,'List Asset' ],
            ],
            'form':produkdijadwalkan_form,
        }

        return render(request, 'minta.html', context)