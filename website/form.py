from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class RegistrationForm(UserCreationForm):
        first_name = forms.CharField(label="First name", max_length=100, initial='Enter your first name')
        last_name = forms.CharField(label="Last name", max_length=100, initial='Enter your last name')
        email = forms.EmailField(label="E-mail", max_length=100, initial='Enter your e-mail address',required=True)
        field_order = ['first_name', 'last_name', 'email']

        def __init__(self, *args, **kwargs):
            super(RegistrationForm, self).__init__(*args, **kwargs)
            self.fields['username'].initial = 'Enter your username'
            self.fields['password1'].initial = 'Enter your password'
            self.fields['password2'].initial = 'Enter again to confirm your password'