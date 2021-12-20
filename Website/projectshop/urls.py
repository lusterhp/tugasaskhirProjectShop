# urls projectshop

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^tambah-asset/$', views.form),
    url(r'^listlapak/$', views.listlapak, name='listlapak'),
    url(r'^listasset/$', views.listasset, name='listasset'),
    url(r'^listgrup/$', views.listgrup, name='listgrup'),
    url(r'^listpp/$', views.listpp, name='listpp'),
    url(r'^tambah-lapak/$', views.form1),
    url(r'^tambah-peralatan/$', views.form3),
    url(r'^tambah-grup/$', views.form4),
    url(r'^tambah-tipe-grup/$', views.form6),
    url(r'^tambah-proses/$', views.form5),
    url(r'^$', views.asset, name='homeasset'),
    url(r'^delete/(?P<hapus_id>[0-9]+)$', views.delete, name='deletelapak'),
    url(r'^update1/(?P<update1_id>[0-9]+)$', views.update1, name='update_lapak'),
    url(r'^updategrup/(?P<updategrup_id>[0-9]+)$', views.updategrup, name='update_grup'),
    url(r'^updateproses/(?P<updateproses_id>[0-9]+)$', views.updateproses, name='update_proses'),
    url(r'^updatealat/(?P<updatealat_id>[0-9]+)$', views.updatealat, name='update_alat'),
    url(r'^deletegrup/(?P<hapusgrup_id>[0-9]+)$', views.deletegrup, name='deletegrup'),
    url(r'^deletealat/(?P<hapusalat_id>[0-9]+)$', views.deletealat, name='deletealat'),
]