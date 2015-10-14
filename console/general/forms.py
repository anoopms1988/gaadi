from django import forms
from .models import Dimensions


class DimensionForm(forms.ModelForm):
    class Meta:
        model = Dimensions
        fields = ['length', 'width', 'height', 'wheelbase', 'bootspace', 'kerbweight']

    length = forms.CharField(label='Length',
                             widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Length'}))
    width = forms.CharField(label='Width',
                            widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Width'}))
    height = forms.CharField(label='Height',
                             widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Height'}))
    wheelbase = forms.CharField(label='Wheelbase', required=False,
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Wheelbase'}))
    bootspace = forms.CharField(label='Bootspace', required=False,
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Bootspace'}))
    kerbweight = forms.CharField(label='Kerbweight', required=False,
                                 widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Kerbweight'}))
