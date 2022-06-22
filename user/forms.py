from django import forms
from .models import *

class SaveBook(forms.ModelForm):
    class Meta:
        model = Books
        fields = ['status']
