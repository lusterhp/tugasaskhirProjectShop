# forms operasi

from django import forms
from django.db.models import fields
from django.forms import ModelForm
from django import forms
from operasi.models import Operasi

class FormOperasi(ModelForm):
    class Meta:
        model = Operasi
        fields = '__all__'

    widgets = {
        'nama_Operasi' : forms.TextInput(attrs={'class':'form-control'}),
        'waktu_mulai' : forms.DateTimeInput(attrs={'class':'form-control'}),
        'waktu_selesai' : forms.DateTimeInput(attrs={'class':'form-control'}),
        'keterangan' : forms.TextInput(attrs={'class':'form-control'}),
        'status_operasi' : forms.BooleanField(attrs={'class':'form-control'}),
        'material_id' : forms.Select(
            attrs={
                'class':'form-control',}
                ),
    }