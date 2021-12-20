# forms model produk

from django import forms
from django.db.models import fields
from django.forms import ModelForm
from django import forms
from models.modelproduk.models import Model

class FormModelProduk(ModelForm):
    class Meta:
        model = Model
        fields = '__all__'

    widgets = {
        'nama_model' : forms.TextInput(attrs={'class':'form-control'}),
        'produk_id' : forms.Select(
            attrs={
                'class':'form-control',}
                ),
    }