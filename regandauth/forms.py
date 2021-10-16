from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class RegisterForm(forms.Form):
    username = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'логин'}))
    email = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'email'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'пароль'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'подтверждение пароля'}))
