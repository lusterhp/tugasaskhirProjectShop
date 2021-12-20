# forms engineering order

from django import forms
from django.db.models import fields
from django.forms import ModelForm
from django import forms
from engineeringorder.models import *

class FormEngineeringOrder(ModelForm):
    class Meta:
        model = EngineeringOrder
        exclude = ['material_id', 'tanggal_diajukan', 'tanggal_berlaku']

        labels = {
            'nama_pengaju':'Nama Pengaju',
            'is_disetujui':'Persetujuan',
            'tanggal_persetujuan':'Tanggal Persetujuan',
            'keterangan' : 'Keterangan',
        }

        widgets = {
            'nama_pengaju' : forms.TextInput(attrs={'class':'form-control'}),
            'is_disetujui' : forms.CheckboxInput,
            'tanggal_persetujuan' : forms.TimeInput(attrs={'class':'form-control', 'type':'date',}),
            'keterangan' : forms.TextInput(attrs={'class':'form-control'}),
        }

class FormEngineeringOrder1(ModelForm):
    class Meta:
        model = EngineeringOrder
        fields = ['nama_pengaju', 'tanggal_persetujuan', 'keterangan',]

        labels = {
            'nama_pengaju':'Nama Pengaju',
            'tanggal_persetujuan':'Tanggal Persetujuan',
            'keterangan' : 'Keterangan',
        }

        widgets = {
            'nama_pengaju' : forms.TextInput(attrs={'class':'form-control'}),
            'tanggal_persetujuan' : forms.TimeInput(attrs={'class':'form-control', 'type':'date',}),
            'keterangan' : forms.TextInput(attrs={'class':'form-control'}),
        }

class FormEngineeringOrder2(ModelForm):
    class Meta:
        model = EngineeringOrder
        fields = ['is_disetujui',]

        labels = {
            'is_disetujui':'Persetujuan',
        }

        widgets = {
            'is_disetujui' : forms.CheckboxInput,
        }