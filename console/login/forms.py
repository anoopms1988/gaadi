from django import forms
from .models import Car, Company,CarType


class LoginForm(forms.Form):
    username = forms.CharField(error_messages={'required': 'Username is required'}, required=True, label='Username',
                               max_length=100,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(error_messages={'required': 'Password is required'}, required=True,
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))


class CarForm(forms.ModelForm):

    company = forms.ChoiceField(choices=[('', 'Select')] + [(o.id, o.name) for o in Company.objects.all()], required=True, widget=forms.Select(attrs={'class': 'form-control'}))
    cartype = forms.ChoiceField(choices=[('', 'Select')] + [(o.id, o.cartype) for o in CarType.objects.all()], required=True, widget=forms.Select(attrs={'class': 'form-control'}))
    name = forms.CharField(error_messages={'required': 'Car name is required'}, required=True,max_length=100,
                               widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter car name'}))
    class Meta:
        model=Car
        fields=['name', 'company', 'cartype']
