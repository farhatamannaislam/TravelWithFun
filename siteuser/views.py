from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import login, authenticate
from .forms import SignUpForm
from .models import UserModel


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            print("Form is valid")
            form.save()
            return redirect('login') 
    else:
        form = SignUpForm()
        print("Form errors:", form.errors)
    return render(request, 'siteuser/signup.html', {'form': form})