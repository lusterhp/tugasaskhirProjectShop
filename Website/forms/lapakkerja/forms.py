# forms lapakkerja

from django import forms
from django.db.models import fields
from django.forms import ModelForm
from django import forms
from models.lapakkerja.models import LapakKerja

class FormLLapakKerja(ModelForm):
    class Meta:
        model = LapakKerja
        fields = '__all__'

    widgets = {
        'nama_lapak' : forms.TextInput(attrs={'class':'form-control'}),
        'availabilitas' : forms.BooleanField(attrs={'class':'form-control'}),
    }