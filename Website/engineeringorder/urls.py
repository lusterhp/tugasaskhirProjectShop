# urls engineering order

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.list, name='listeo'),
    url(r'^formeo/$', views.form, name='formeo'),
    url(r'^delete/(?P<delete_id>[0-9]+)$', views.delete, name='deleteeo'),
    url(r'^update1/(?P<update1_id>[0-9]+)$', views.update1, name='update_eo'),
    url(r'^update2/(?P<update2_id>[0-9]+)$', views.update2, name='update_meo'),
    url(r'^detail-list/(?P<dlid>[0-9]+)$', views.detail_list, name='detail_list'),
    url(r'^update3/(?P<update3_id>[0-9]+)$', views.update3, name='update_persetujuan'),
]
