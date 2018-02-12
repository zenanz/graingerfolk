from django.contrib.auth.forms import UserCreationForm, PasswordResetForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import *
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

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['profile_photo', 'birthday', 'country', 'state']

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

class EmailValidationOnForgotPassword(PasswordResetForm):
    def clean_email(self):
        email = self.cleaned_data['email']
        if not User.objects.filter(email__iexact=email, is_active=True).exists():
            raise ValidationError("There is no user registered with the specified email address!")
        return email