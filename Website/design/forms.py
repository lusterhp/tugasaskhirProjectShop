# forms design

from django import forms
from django.db.models import fields
from django.forms import ModelForm
from django import forms
from design.models import *
from engineeringorder.models import *

class FormMaterialEO(forms.ModelForm):
    class Meta:
        model = MaterialEO
        exclude = ['is_berlaku', 'keterangan', 'tanggalGanti']

        labels = {
            'kode_eo' : 'Kode Engineering Order',
            'varian_id':'Produk',
            'id_materialeo':'ID Material',
            'nama_material':'Nama Material',
            'nama_supplier':'Nama Supplier',
            'penyusun_produk':'Material Lain yang Disusun',
            'tanggal_berlaku':'Tanggal Material Mulai Berlaku',
            'penggantiMaterial':'Material yang Diganti',
        }
        widgets = {
            'kode_eo': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Masukkan Kode Engineering Order',
                }
            ),
            'varian_id': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),
            'id_materialeo': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Masukkan ID material',
                }
            ),
            'nama_material': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Masukkan nama material',
                }
            ),
            'nama_supplier': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Masukkan nama supplier',
                }
            ),
            'penyusun_produk': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),
            'tanggal_berlaku': forms.TimeInput(
                attrs={
                    'class': 'form-control',
                    'type': 'date',
                }
            ),
            'penggantiMaterial' : forms.Select(
            attrs={
                'class':'form-control',}
                ),            
        }

class FormMaterial(forms.ModelForm):
    class Meta:
        model = Material
        fields = [
            'varian_id',
            'id_material',
            'nama_material',
            'nama_supplier',
            'penyusun_produk',
            'tanggal_berlaku',
        ]

        labels = {
            'varian_id':'Produk',
            'id_material':'ID Material',
            'nama_material':'Nama Material',
            'nama_supplier':'Nama Supplier',
            'penyusun_produk':'Material Lain yang Disusun',
            'tanggal_berlaku':'Tanggal Material Mulai Berlaku',
        }
        widgets = {
            'varian_id': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),
            'id_material': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Masukkan ID material',
                }
            ),
            'nama_material': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Masukkan nama material',
                }
            ),
            'nama_supplier': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Masukkan nama supplier',
                }
            ),
            'penyusun_produk': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),
            'tanggal_berlaku': forms.TimeInput(
                attrs={
                    'class': 'form-control',
                    'type': 'date',
                }
            ),
        }

class FormProses(forms.ModelForm):
    class Meta:
        model = Proses
        fields ='__all__'
        labels = {
            'id_proses':'ID Proses',
            'nama_proses':'Nama Proses',
            'varian_id':'Produk',
            'material_id':'Material yang Dikerjakan',
            'peralatan_id':'Peralatan yang Diperlukan (Tekan "control" atau "command" untuk Memilih Lebih dari Satu)',
            'grup_id':'Grup Kerja yang Dibutuhkan',
            'durasi': 'Durasi Proses (dalam menit)',
            'tahapan_pengerjaan': 'Tahapan',
        }
        widgets = {
            'id_proses': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Masukkan ID proses',
                }
            ),
            'nama_proses': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Masukkan nama proses',
                }
            ),
            'varian_id': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),
            'material_id': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),
            'peralatan_id': forms.SelectMultiple(
                attrs={
                    'class': 'form-control',
                }
            ),
            'grup_id': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),
            'durasi': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Masukkan durasi proses dalam satuan menit',
                }
            ),
            'tahapan_pengerjaan': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Masukkan tahapan',
                }
            ),
        }