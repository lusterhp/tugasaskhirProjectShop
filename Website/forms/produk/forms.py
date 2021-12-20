# forms produk

from django import forms
from django.db.models import fields
from django.forms import ModelForm
from django import forms
from models.produk.models import Produk

class FormProduk(ModelForm):
    class Meta:
        model = Produk
        fields = '__all__'

    widgets = {
        'nama_produk' : forms.TextInput(attrs={'class':'form-control'}),
    }