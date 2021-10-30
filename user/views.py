from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import ProfileUpdateForm,UserRegistrationForm,UserUpdateForm
from django.contrib.auth.decorators import login_required
from .models import Profile
# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request,f'Your Account has been created!, You are now able to login')
            return redirect('login')
    else:
        form = UserRegistrationForm()
        return render(request,'register.html',{'form':form})
@login_required
def profile(request):
    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        profile = Profile(user=request.user)
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST,instance=request.user)
        p_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
    else:
        p_form = ProfileUpdateForm(instance=request.user.profile)
        u_form = UserUpdateForm(instance=request.user)
        
    context = {
        'u_form' : u_form,
        'p_form' : p_form,

    }
    return render(request,'profile.html',context)
