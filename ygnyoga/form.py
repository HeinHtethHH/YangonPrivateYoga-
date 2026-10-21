from django import forms
from .models import Ygnyoga

class ygnyoga(forms.ModelForm):
    
    class Meta:
        model = Ygnyoga
        fields = [
             'title','image1','image2','image3','reserved1','reserved2','reserved3'
        ]
