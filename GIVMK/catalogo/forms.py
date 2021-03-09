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
                'class': 'form-control',
                'placeholder': 'Nombre del Producto a Registrar'
            }),
            'precio_consultora': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '0.00',
                'aria-describedby': 'basic-addon1'
            }),
            'precio_catalogo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '0.00'
            }),
            'descripcion': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': '3',
                'placeholder': 'Ingrese una descripcion del producto'
            }),
        #     'NIT': forms.DateInput(attrs={
        #         'class': 'form-control'
        #     }),
        #     'tel': forms.DateInput(attrs={
        #         'class': 'form-control'
        #     }),
        }