# forms produk

from django import forms
from django.db.models import fields
from django.forms import ModelForm
from django import forms
from .models import *

class FormProduk(forms.ModelForm):
    class Meta:
        model = Produk
        fields ='__all__'
        labels = {
            'id_brand': 'ID Brand',
            'nama_brand': 'Nama Brand',
            'id_model': 'ID Model',
            'nama_model':'Nama Model',
            'id_varian': 'ID Varian',
            'nama_varian':'Nama Varian',
            'nama_atribut':'Nama Atribut',
            'nilai_atribut':'Nilai Atribut',
        }

        widgets = {
        'id_brand': forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Masukkan ID brand',
            }
        ),
        'nama_brand': forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Masukkan nama brand',
            }
        ),
        'id_model': forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Masukkan ID model',
            }
        ),
        'nama_model': forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Masukkan nama model',
            }
        ),
        'id_varian': forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Masukkan ID varian',
            }
        ),
        'nama_varian': forms.TextInput(
            attrs = {
                'class':'form-control',
                'placeholder':'Masukkan nama varian',
            }
        ),
        'nama_atribut': forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Masukkan nama atribut',
            }
        ),
        'nilai_atribut': forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Masukkan nilai atribut',
            }
        ),
    }

class FormBrand(forms.ModelForm):
    class Meta:
        model = Brand
        fields ='__all__'
        labels = {
            'id_brand': 'ID Brand',
            'nama_brand': 'Nama Brand',
        }

        widgets = {
        'id_brand': forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Masukkan ID brand',
            }
        ),
        'nama_brand': forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Masukkan nama brand',
            }
        ),
    }

class FormModel(ModelForm):
    class Meta:
        model = Model
        fields = '__all__'

        labels = {
            'id_model': 'ID Model',
            'nama_model':'Nama Model',
        }

        widgets = {
        'id_model': forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Masukkan ID model',
            }
        ),
        'nama_model': forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Masukkan nama model',
            }
        ),
    }

class FormVariant(forms.ModelForm):
    class Meta:
        model = Variant
        fields = '__all__'
        labels = {
            'id_varian': 'ID Varian',
            'nama_varian':'Nama Varian',
            'nama_atribut':'Nama Atribut',
            'nilai_atribut':'Nilai Atribut',
        }

        widgets = {
        'id_varian': forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Masukkan ID varian',
            }
        ),
        'nama_varian': forms.TextInput(
            attrs = {
                'class':'form-control',
                'placeholder':'Masukkan nama varian',
            }
        ),
        'nama_atribut': forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Masukkan nama atribut',
            }
        ),
        'nilai_atribut': forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Masukkan nilai atribut',
            }
        ),
    }


class FormMaterial(ModelForm):
    class Meta:
        model = Material
        fields = '__all__'

    widgets = {
        'nama_material' : forms.TextInput({'class':'form-control'}),
        'nama_supplier' : forms.TextInput({'class':'form-control'}),
        'penyusun_produk' : forms.TextInput({'class':'form-control'}),
        'is_diubah' : forms.BooleanField(required=False),
        'tanggal_material_dibuah' : forms.DateField({'class':'form-control'}),
        'keterangan' : forms.TextInput({'class':'form-control'}),
    }

class FormProdukDijadwalkan(ModelForm):
    class Meta:
        model = ProdukDijadwalkan
        exclude = ['lapak_id',]
        labels = {
            'id_pesanan': 'ID Pesanan',
            'nama_pesanan': 'Nama Pesanan',
            'produk_id':'Produk',
            'deadline_diminta':'Permintaan Deadline',
            'status_pengerjaan': 'Status',
        }
        widgets = {
        'id_pesanan': forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Masukkan ID Pesanan',
                }
            ),
        'nama_pesanan': forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Masukkan Nama Pesanan',
                }
            ),
        'produk_id': forms.Select(
            attrs={
                'class': 'form-control',
                'placeholder': 'Pilih ID Produk',
            }
        ),
        'deadline_diminta': forms.DateTimeInput(
            attrs={
                'class': 'form-control',
                'type':'date',
            }
        ),
        'status_pengerjaan': forms.Select(
            attrs={
                'class': 'form-control',
            }
        ),
    }