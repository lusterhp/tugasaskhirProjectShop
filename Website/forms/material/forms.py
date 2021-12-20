# forms material

from django import forms
from django.db.models import fields
from django.forms import ModelForm
from django import forms
from models.material.models import Material

class FormMaterial(ModelForm):
    class Meta:
        model = Material
        fields = '__all__'

    widgets = {
        'kode_material' : forms.TextInput(attrs={'class':'form-control'}),
        'nama_material' : forms.TextInput(attrs={'class':'form-control'}),
        'nama_supplier' : forms.TextInput(attrs={'class':'form-control'}),
        'variant_id' : forms.Select(
            attrs={
                'class':'form-control',}
                ),
        'tanggal_ditambahkan' : forms.DateTimeInput(attrs={'class':'form-control'}),
        "is_diubah" : forms.BooleanField(attrs={'class':'form-control'}),
        'tanggal_material_diubah' : forms.DateTimeInput(attrs={'class':'form-control'}),
        'keterangan' : forms.TextInput(attrs={'class':'form-control'}),
        'proses_id' : forms.Select(
            attrs={
                'class':'form-control',}
                ),
    }