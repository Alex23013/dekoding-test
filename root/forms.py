
from django.forms import ModelForm
from django import forms

class DogForm(forms.Form):
    name = forms.CharField(label='Name', max_length=42)
    breed = forms.CharField(label='Breed', max_length=42)
    age = forms.IntegerField(label='Age')
    owner = forms.CharField(label = 'Owner', max_length=42)

