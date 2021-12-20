# urls produk

from django.conf.urls import url
from . import views
from produk import viewsganttchart

urlpatterns = [
    url(r'^delete1/(?P<delete1_id>[0-9]+)$', views.delete1, name='deleteproduk'),
    url(r'^delete2/(?P<delete2_id>[0-9]+)$', views.delete2, name='deletemodel'),
    url(r'^tambah/$', views.tambah),
    url(r'^tambah-produk/$', views.produk, name='formproduk'),
    url(r'^tambah-produkdijadwalkan/$', views.penjadwalanoperasi, name='formprodukdijadwalkan'),
    url(r'^jadwal-operasi/(?P<idpd>[0-9]+)$', viewsganttchart.jadwaloperasi, name='jadwaloperasi'),
    url(r'^tambah-model/$', views.model, name='formmodel'),
    url(r'^minta-jadwal-produk/$', views.produkdijadwalkan, name='listprodukdijadwalkan'),
    url(r'^$', views.list, name='listproduk'),
    url(r'^delete/(?P<delete_id>[0-9]+)$', views.delete, name='deleteprodukdijadwalkan'),
    url(r'^update/(?P<update_id>[0-9]+)$', views.update, name='update_produkdijadwalkan'),
    url(r'^list-produk-dijadwalkan/$', views.listprodukdijadwalkan, name='produkdijadwalkan'),
    url(r'^homeproduk/$', views.homeproduk, name='homeproduk'),
    url(r'^update1/(?P<update1_id>[0-9]+)$', views.update1, name='update_produk'),
    url(r'^update2/(?P<update2_id>[0-9]+)$', views.update2, name='update_model'),
]
