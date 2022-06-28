from unicodedata import name
from django import forms

class CountryForm(forms.Form):
    
    country_name = forms.CharField(label='Pais', max_length=100, min_length=3)
    code = forms.CharField(label='Codigo', max_length=3, min_length=3)    
    