from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import ProfileModel
from django import forms

class SiteuserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','email']
    def __init__(self, *args, **kwargs):
        super(SiteuserUpdateForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'email']:
            self.fields[fieldname].help_text = None

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        fields = ['image']
