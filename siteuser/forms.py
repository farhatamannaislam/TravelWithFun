from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserModel
from django import forms


class SignUpForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']