# urls order

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.list),
    url(r'^form/$', views.form),
]
