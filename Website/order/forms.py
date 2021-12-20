# forms order

from django import forms
from django.db.models import fields
from django.forms import ModelForm
from django import forms
from .models import *

class FormPenjadwalan(ModelForm):
    class Meta:
        model = ProsesKerja
        fields = '__all__'

    widgets = {
        'nama_proses' : forms.TextInput(
            attrs = {
                'class':'form-control',}
                ),

        'material_id' : forms.Select(
            attrs={
                'class':'form-control',}
                ),

        'peralatankerja_id' : forms.Select(
            attrs={
                'class':'form-control',}
                ),

        'waktu_mulai' : forms.DateTimeInput(
            attrs={
                'class':'form-control',}
                ),

        'waktu_selesai' : forms.DateTimeInput(
            attrs={
                'class':'form-control',}
                ),

        'produk_id' : forms.Select(
            attrs={
                'class':'form-control',}
                ),
                
        'lapakkerja_id' : forms.Select(
            attrs={
                'class':'form-control',}
                ),
    }