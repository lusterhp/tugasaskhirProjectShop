# forms projectshop

from django import forms
from django.db.models import fields
from django.forms import ModelForm
from django import forms
from .models import *

class FormProses(ModelForm):
    class Meta:
        model = ProsesKerja
        fields = '__all__'
        labels = {
            'kode_proses': 'ID Proses',
            'nama_proses': 'Nama Proses',
            'peralatan_id': 'Alat yang Dibutuhkan',
            'grup_id': 'Grup Kerja Pengampu',
        }

        widgets = {
        'kode_proses': forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Masukkan ID Proses',
            }
        ),
        'nama_proses': forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Masukkan Nama Proses',
            }
        ),
        'peralatan_id':forms.Select(
            attrs={
                'class':'form-control',
            }
        ),
        'grup_id':forms.Select(
            attrs={
                'class':'form-control',
            }
        ),
    }

class FormTipeGrup(ModelForm):
    class Meta:
        model = TipeKerja
        fields = '__all__'
        labels = {
            'tipe_grup' : 'Tipe Grup Kerja',
        },
        widgets = {
            'tipe_grup' : forms.TextInput(
                attrs={
                    'class' : 'form-control',
                    'placeholder' : 'Tipe Grup Kerja',
                },
            ),
        },

class FormGrup(ModelForm):
    class Meta:
        model = GrupKerja
        exclude = ['aktif_bekerja', 'jamkerja_pekerja']
        labels = {
            'kode_grup': 'Pilih Tipe Grup Kerja',
            'nama_grup': 'Nama Grup Kerja',
            'jumlah_pekerja': 'Jumlah Pekerja',
            'nama_personil' : 'Nama-nama Personil',
        }

        widgets = {
        'kode_grup': forms.Select(
            attrs={
                'class': 'form-control',
            }
        ),
        'nama_grup': forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Masukkan Nama Grup Kerja',
            }
        ),
        'jumlah_pekerja': forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Masukkan Jumlah Pekerja',
            }
        ),
        'nama_personil': forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Masukkan Nama-Nama Personil',
            }
        ),
    }

class FormLapak(ModelForm):
    class Meta:
        model = LapakKerja
        exclude = ['jadwal_lapak',]
        labels = {
            'kode_lapak': 'ID Lapak Kerja',
            'nama_lapak': 'Nama Lapak Kerja',
            'aktif_bekerja' : 'Aktif Bekerja',
        }

        widgets = {
        'kode_lapak': forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Masukkan ID Lapak Kerja',
            }
        ),
        'nama_lapak': forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Masukkan Nama Lapak Kerja',
            }
        ),
        'aktif_bekerja': forms.CheckboxInput(
            
        ),
    }

class FormAlat(ModelForm):
    class Meta:
        model = PeralatanKerja
        fields = '__all__'
        labels = {
            'kode_alat': 'ID Peralatan Kerja',
            'nama_alat': 'Nama Peralatan Kerja'
        }

        widgets = {
        'kode_alat': forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Masukkan ID Peralatan Kerja',
            }
        ),
        'nama_alat': forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Masukkan Nama Peralatan Kerja',
            }
        ),
    }