from django.shortcuts import render, redirect
#from .forms import ProfileUpdateForm
from django.contrib.auth.decorators import login_required
import os
# Create your views here.
#@login_required
def profile(request):
    # if request.method == 'POST':
    #     u_form = UserUpdateForm(request.POST or None, instance=request.user)
    #     p_form = ProfileUpdateForm(
    #         request.POST or None, request.FILES or None, instance=request.user.profilemodel)
    #     if u_form.is_valid() and p_form.is_valid():
    #         u_form.save()
    #         p_form.save()
    #         return redirect('users-profile')
    # else:
    #     u_form = UserUpdateForm(instance=request.user)
    #     p_form = ProfileUpdateForm(instance=request.user.profilemodel)
    # context = {
    #     'u_form': u_form,
    #     'p_form': p_form,
    # }
    return render(request, 'siteuser/profile.html')