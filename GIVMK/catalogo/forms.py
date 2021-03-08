from django import forms
from django.forms import ModelForm
from .models import Producto
from datetime import datetime

class ProductoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['autocomplete'] = 'off'

    class Meta:
        model = Producto
        fields = 'nombre', 'precio_consultora', 'precio_catalogo', 'descripcion', 'img'
        widgets = {
        #     'nacimiento': forms.DateInput(format='%Y-%m-%d',
        #         attrs={
        #         'value': datetime.now().strftime('%Y-%m-%d'),
        #         'class': 'form-control'
        #         }),
            'nombre': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'precio_consultora': forms.NumberInput(attrs={
                'class': 'form-control'
            }),
            'precio_catalogo': forms.NumberInput(attrs={
                'class': 'form-control'
            }),
            'descripcion': forms.Textarea(attrs={
                'class': 'form-control'
            }),
        #     'NIT': forms.DateInput(attrs={
        #         'class': 'form-control'
        #     }),
        #     'tel': forms.DateInput(attrs={
        #         'class': 'form-control'
        #     }),
        }