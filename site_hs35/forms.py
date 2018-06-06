from django import forms
from django.forms import ModelForm

from .models import Ankete

class AnketeForm(forms.ModelForm):
    class Meta:
        model = Ankete
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.TextInput(attrs={'class': 'select-dropdown'}),
            'discipline': forms.TextInput(attrs={'class': 'select-dropdown'}),
            'wishes': forms.TextInput(attrs={'class': 'form-control'}),
        }
