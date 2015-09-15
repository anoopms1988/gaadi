from django import forms
from .models import Car, Company


class LoginForm(forms.Form):
    username = forms.CharField(error_messages={'required': 'Username is required'}, required=True, label='Username',
                               max_length=100,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(error_messages={'required': 'Password is required'}, required=True,
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))


class CarForm(forms.ModelForm):

    class Meta:
        model = Car
        fields = ['name','company','type']

        company=forms.ModelChoiceField(queryset=Company.objects.all())
      
