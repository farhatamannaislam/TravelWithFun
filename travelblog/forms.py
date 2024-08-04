from django import forms
from .models import Post
from django.contrib.auth.models import User

class PostForm(forms.ModelForm):
    author = forms.ModelChoiceField(
        queryset=User.objects.all(),
        required=True,
        widget=forms.Select,
        empty_label="Select Author"
    )

    class Meta:
        model = Post
        fields = ['title', 'slug', 'content', 'status', 'author']