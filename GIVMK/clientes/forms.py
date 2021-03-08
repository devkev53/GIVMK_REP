from django import forms
from django.forms import ModelForm
from .models import Client
from datetime import datetime

class ClienteForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
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
            'firts_name': forms.DateInput(attrs={
                'class': 'form-control'
            }),
            'last_name': forms.DateInput(attrs={
                'class': 'form-control'
            }),
            'gender': forms.Select(attrs={
                'class': 'form-control'
            }),
            'idNumber': forms.DateInput(attrs={
                'class': 'form-control'
            }),
            'NIT': forms.DateInput(attrs={
                'class': 'form-control'
            }),
            'tel': forms.DateInput(attrs={
                'class': 'form-control'
            }),
        }