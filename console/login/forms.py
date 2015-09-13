from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(error_messages={'required': 'Username is required'}, required=True, label='Username',
                               max_length=100,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(error_messages={'required': 'Password is required'}, required=True,
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
