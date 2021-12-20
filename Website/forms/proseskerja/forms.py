# forms proseskerja

from django import forms
from django.db.models import fields
from django.forms import ModelForm
from django import forms
from models.proseskerja.models import Proses

class FormProses(ModelForm):
    class Meta:
        model = Proses
        fields = '__all__'

    widgets = {
        'nama_proses' : forms.TextInput(attrs={'class':'form-control'}),
        'kebutuhan_alat' : forms.TextInput(attrs={'class':'form-control'}),
    }