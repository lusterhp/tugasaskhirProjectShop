# forms engineering order

from django import forms
from django.db.models import fields
from django.forms import ModelForm
from django import forms
from models.engineeringorder.models import *

class FormEngineeringOrder(ModelForm):
    class Meta:
        model = EngineeringOrder
        fields = '__all__'

    widgets = {
        'nama_pengaju' : forms.TextInput(attrs={'class':'form-control'}),
        'tanggal_diajukan' : forms.DateTimeInput(attrs={'class':'form-control'}),
        'is_disetujui' : forms.BooleanField(required=False),
        'tanggal_persetujuan' : forms.DateTimeInput(attrs={'class':'form-control'}),
        'tanggal_mulai_berlaku' : forms.DateTimeInput(attrs={'class':'form-control'}),
        'keterangan' : forms.TextInput(attrs={'class':'form-control'}),
        'material_id' : forms.Select(
            attrs={
                'class':'form-control',}
                ),
    }