from django.forms import ModelForm
from django import forms
from .models import Pedido

from datetime import datetime

class PedidoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'
            form.field.widget.attrs['autocomplete'] = 'off'
        self.fields['totalConsultora'].label = "Total Pedido Precio Consultora"
        self.fields['totalCatalogo'].label = "Total Pedido Precio Catalógo"

        self.fields['totalConsultora'].widget.attrs = {
            'class': 'form-control',
            'readonly': True,
            'disable': True
        }
        self.fields['totalCatalogo'].widget.attrs={
            'class': 'form-control',
            'readonly': True,
            'disable': True
        }
        self.fields['referencia'].widget.attrs = {
            'placeholder': 'Referencia de Pedido',
            'class': 'form-control',
            'autocomplete': 'off'
        }

    class Meta:
        model = Pedido
        fields = '__all__'
        widgets = {
            'fecha': forms.DateInput(
                format='%Y-%m-%d',
                attrs={
                    'class': 'form-control',
                    'value': datetime.now().strftime('%Y-%m-%d'),
                    'readonly': True,
                }),
        }
