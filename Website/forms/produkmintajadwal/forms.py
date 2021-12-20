# forms produk yang dimintakan penjadwalan

from django import forms
from django.db.models import fields
from django.forms import ModelForm
from django import forms
from produk.models import ProdukDijadwalkan

class FormProdukDijadwalkan(ModelForm):
    class Meta:
        model = ProdukDijadwalkan
        fields = '__all__'

    widgets = {
        'status_design' : forms.BooleanField(attrs={'class':'form-control'}),
        'status_operasi' : forms.BooleanField(attrs={'class':'form-control'}),
        'variant_id' : forms.Select(
            attrs={
                'class':'form-control',}
                ),
    }