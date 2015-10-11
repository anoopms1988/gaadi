from django import forms
from .models import Dimensions


class DimensionForm(forms.Form):
    class Meta:
        model = Dimensions
        fields = ['length', 'width']

    length = forms.CharField(label='Length',
                              widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Length'}))
    width = forms.CharField(label='Width',
                             widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Width'}))
    height = forms.CharField(label='Height',
                              widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Height'}))
    wheelbase = forms.CharField(label='Wheelbase',
                              widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Wheelbase'}))
    bootspace = forms.CharField(label='Bootspace',
                              widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Bootspace'}))
    kerbweight = forms.CharField(label='Kerbweight',
                              widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Kerbweight'}))