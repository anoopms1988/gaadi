from django import forms
from .models import Dimensions,Brake
from console.login.models import Engine


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


class EngineForm(forms.ModelForm):
    class Meta:
        model = Engine
        fields = ['torque', 'displacement', 'power', 'cylinders', 'valvespercylinder', 'valvemechanism',
                  'cylinderconfiguration']

    torque = forms.CharField(label='Torque',required=False,
                             widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Torque'}))
    displacement = forms.CharField(label='Displacement',required=False,
                             widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Displacement'}))
    power = forms.CharField(label='Power',required=False,
                             widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Power'}))
    cylinders=forms.CharField(label='Cylinders',required=False,
                             widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Cylinders'}))
    valvespercylinder=forms.CharField(label='Valvespercylinder',required=False,
                             widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Valvespercylinder'}))
    valvemechanism=forms.CharField(label='Valvemechanism',required=False,
                             widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Valvemechanism'}))
    cylinderconfiguration=forms.CharField(label='Cylinder configuration',required=False,
                             widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Cylinder configuration'}))

class BrakeForm(forms.ModelForm):
    class Meta:
        model = Brake
        fields = ['rear_brakes', 'front_brakes']

    rear_brakes = forms.CharField(label='Rear brakes',required=False,
                             widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Rear brakes'}))
    front_brakes = forms.CharField(label='Front brakes',required=False,
                             widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Front brakes'}))
