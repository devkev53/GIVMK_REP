from django import forms
from django.forms import ModelForm
from .models import Client
from datetime import datetime

class ClienteForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'
            form.field.widget.attrs['autocomplete'] = 'off'
        self.fields['estado'].widget.attrs = {
            'hidden': 'true',
        }


    class Meta:
        model = Client
        fields = '__all__'
        widgets = {
            'nacimiento': forms.DateInput(format='%Y-%m-%d',
                attrs={
                'value': datetime.now().strftime('%Y-%m-%d'),
                'class': 'form-control'
                }),
        }