from django.shortcuts import render, redirect
from .forms import ProfileUpdateForm, SiteuserUpdateForm
from django.contrib.auth.decorators import login_required

@login_required
def profile(request):
    """
    Display user Profile and process user's profile update form.
    **Context:**

    - `u_form`: An instance of :form:`siteuser.SiteuserUpdateForm`
    - `p_form`: An instance of :form:`siteuser.ProfileUpdateForm`
    **Template:**

    :template:`siteuser/profile.html`
    """  
    if request.method == 'POST':
        u_form = SiteuserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profilemodel)
        
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('siteuser-profile')
    else:
        u_form = SiteuserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profilemodel)

    context = {
        'u_form': u_form,
        'p_form': p_form,
    }
    return render(request, 'siteuser/profile.html', context)
