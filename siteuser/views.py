from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

def signup(request):
    form = UserCreationForm()
    context = {
        'form':form
    }
    return render(request,'siteuser/signup.html')
    