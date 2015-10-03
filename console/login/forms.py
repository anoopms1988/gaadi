from django import forms
from .models import Car, Company, CarType, Variant, Fuel, Dealer
from .fields import NameModelChoiceField, CartypeModelChoiceField


class LoginForm(forms.Form):
    username = forms.CharField(error_messages={'required': 'Username is required'}, required=True, label='Username',
                               max_length=100,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(error_messages={'required': 'Password is required'}, required=True,
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['name', 'description']

    company = NameModelChoiceField(error_messages={'required': 'Company is required'}, queryset=Company.objects.all(),
                                   widget=forms.Select(attrs={'class': 'form-control', 'id': 'company'}),
                                   empty_label='Select')
    cartype = CartypeModelChoiceField(error_messages={'required': 'Company is required'},
                                      queryset=CarType.objects.all(),
                                      widget=forms.Select(attrs={'class': 'form-control', 'id': 'cartype'}),
                                      empty_label='Select')
    name = forms.CharField(error_messages={'required': 'Car name is required'}, required=True, max_length=100,
                           widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter car name'}))
    description = forms.CharField(required=False, widget=forms.Textarea(
        attrs={'class': 'form-control', 'placeholder': 'Enter car description'}))


class VariantForm(forms.ModelForm):
    class Meta:
        model = Variant
        fields = ['name']

    company = NameModelChoiceField(error_messages={'required': 'Company is required'}, queryset=Company.objects.all(),
                                   widget=forms.Select(attrs={'class': 'form-control', 'id': 'company'}),
                                   empty_label='Select')

    car = NameModelChoiceField(error_messages={'required': 'Car is required'}, queryset=Car.objects.all(),
                               widget=forms.Select(attrs={'class': 'form-control', 'id': 'car'}),
                               empty_label='Select')
    fuel = NameModelChoiceField(error_messages={'required': 'Fuel type is required'}, queryset=Fuel.objects.all(),
                                widget=forms.Select(attrs={'class': 'form-control', 'id': 'fuel'}),
                                empty_label='Select')
    name = forms.CharField(error_messages={'required': 'Variant name is required'}, required=True, max_length=100,
                           widget=forms.TextInput(
                               attrs={'class': 'form-control', 'placeholder': 'Enter variant name'}))


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['name', 'logo', 'description']

    name = forms.CharField(error_messages={'required': 'Company name is required'}, required=True, label='Companyname',
                           max_length=100,
                           widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Companyname'}))
    description = forms.CharField(required=False, widget=forms.Textarea(
        attrs={'class': 'form-control', 'placeholder': 'Enter company description'}))
    logo = forms.FileField(widget=forms.FileInput)


class DealerForm(forms.ModelForm):
    class Meta:
        model = Dealer
        fields = ['name', 'city', 'address', 'phonenumber', 'mobilenumber', 'email', 'openinghours']


    name = forms.CharField(error_messages={'required': 'Dealer name is required'}, required=True, label='Dealername',
                           max_length=100,
                           widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Dealername'}))
    city = forms.CharField(error_messages={'required': 'City name is required'}, required=True, label='City',
                           max_length=100,
                           widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'City'}))
    address = forms.CharField(required=False, widget=forms.Textarea(
        attrs={'class': 'form-control', 'placeholder': 'Enter address'}))
    phonenumber = forms.CharField(error_messages={'required': 'Phone number is required'}, required=True,
                                  label='Phone number',
                                  max_length=100,
                                  widget=forms.TextInput(
                                      attrs={'class': 'form-control', 'placeholder': 'Phone number'}))
    mobilenumber = forms.CharField(error_messages={'required': 'Mobile number is required'}, required=True,
                                   label='Mobile number',
                                   max_length=100,
                                   widget=forms.TextInput(
                                       attrs={'class': 'form-control', 'placeholder': 'Mobile number'}))
    email = forms.EmailField(error_messages={'required': 'Mobile number is required'}, required=True, label='Email',
                             max_length=100,
                             widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    openinghours = forms.CharField(error_messages={'required': 'Opening hours is required'}, required=True,
                                   label='Opening hours',
                                   max_length=100,
                                   widget=forms.TextInput(
                                       attrs={'class': 'form-control', 'placeholder': 'Opening hours'}))
