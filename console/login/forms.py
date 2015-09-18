from django import forms
from .models import Car, Company, CarType, Variant, Fuel


class LoginForm(forms.Form):
    username = forms.CharField(error_messages={'required': 'Username is required'}, required=True, label='Username',
                               max_length=100,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(error_messages={'required': 'Password is required'}, required=True,
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['name', 'company', 'cartype', 'description']

    company = forms.ChoiceField(error_messages={'required': 'Company name is required'},
                                choices=[('', 'Select')] + [(o.id, o.name)
                                                            for o in Company.objects.all()],
                                required=True, widget=forms.Select(attrs={'class': 'form-control '}))
    cartype = forms.ChoiceField(error_messages={'required': 'Cartype is required'},
                                choices=[('', 'Select')] + [(o.id, o.cartype)
                                                            for o in CarType.objects.all()],
                                required=True, widget=forms.Select(attrs={'class': 'form-control'}))
    name = forms.CharField(error_messages={'required': 'Car name is required'}, required=True, max_length=100,
                           widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter car name'}))
    description = forms.CharField(required=False, widget=forms.Textarea(
        attrs={'class': 'form-control', 'placeholder': 'Enter car description'}))


class VariantForm(forms.ModelForm):
    class Meta:
        model = Variant
        fields = ['car', 'fuel', 'name']

    company = forms.ChoiceField(error_messages={'required': 'Company name is required'},
                                choices=[('', 'Select')] + [(o.id, o.name)
                                                            for o in Company.objects.all()],
                                required=True, widget=forms.Select(attrs={'class': 'form-control ', 'id': 'company'}))

    car = forms.ChoiceField(error_messages={'required': 'Car name is required'},
                            choices=[('', 'Select')] + [(o.id, o.name)
                                                        for o in Car.objects.all()],
                            required=True, widget=forms.Select(attrs={'class': 'form-control ', 'id': 'car'}))
    fuel = forms.ChoiceField(error_messages={'required': 'fuel type is required'},
                             choices=[('', 'Select')] + [(o.id, o.name)
                                                         for o in Fuel.objects.all()],
                             required=True, widget=forms.Select(attrs={'class': 'form-control'}))
    name = forms.CharField(error_messages={'required': 'Variant name is required'}, required=True, max_length=100,
                           widget=forms.TextInput(
                               attrs={'class': 'form-control', 'placeholder': 'Enter variant name'}))
