from django.shortcuts import render, redirect
from .forms import ProfileUpdateForm, UserUpdateForm
from django.contrib.auth.decorators import login_required

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profilemodel)
        
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('siteuser-profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profilemodel)

    context = {
        'u_form': u_form,
        'p_form': p_form,
    }
    return render(request, 'siteuser/profile.html', context)
