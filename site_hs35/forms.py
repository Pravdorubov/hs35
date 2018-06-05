from django import forms
from django.forms import ModelForm

from .models import Ankete

class AnketeForm(forms.ModelForm):
    class Meta:
        model = Ankete
        fields = '__all__'

