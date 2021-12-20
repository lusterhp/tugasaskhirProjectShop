# forms variant

from django import forms
from django.db.models import fields
from django.forms import ModelForm
from django import forms
from models.variant.models import Variant

class FormVariant(ModelForm):
    class Meta:
        model = Variant
        fields = '__all__'

    widgets = {
        'nama_variant' : forms.TextInput(attrs={'class':'form-control'}),
        'nama_atribut' : forms.TextInput(attrs={'class':'form-control'}),
        'nilai_atribut' : forms.TextInput(attrs={'class':'form-control'}),
        'model_id' : forms.Select(
            attrs={
                'class':'form-control',}
                ),
    }