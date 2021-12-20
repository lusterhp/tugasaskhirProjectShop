# urls design

"""TA URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from os import name
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.list1, name='list1'),
    url(r'^list/(?P<idVarianInput>[\w-]+)/$', views.list, name='list'),
    url(r'^formmaterial/$', views.form2, name='formmaterial'),
    url(r'^formproses/$', views.form, name='formproses'),
    url(r'^delete2/(?P<hapus_id>[0-9]+)$', views.delete2, name='delete2'),
    url(r'^deleteproses/(?P<hapusproses_id>[0-9]+)$', views.deleteproses, name='deleteproses'),
    url(r'^update2/(?P<update_id>[0-9]+)/$', views.updateMaterial, name='update_material'),
]
