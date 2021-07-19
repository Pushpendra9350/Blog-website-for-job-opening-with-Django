from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import userRegisterForm, userUpdateForm, profileUpdateForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request):
    if request.method == "POST":
        form = userRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request,f"Account created with username {username}! Now login")
            return redirect("login")
    else:
        form = userRegisterForm()
    return render(request,"userapp/register.html",{"form":form})

@login_required
def profile(request):
    if request.method == "POST":
        u_form = userUpdateForm(request.POST, instance = request.user)
        p_form = profileUpdateForm(request.POST,request.FILES, instance = request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request,f"Account has been updated!")
            return redirect("profile")

    else:
        u_form = userUpdateForm(instance = request.user)
        p_form = profileUpdateForm(instance = request.user.profile)
    # u_form = userUpdateForm()
    # p_form = profileUpdateForm()
    context = {
        'u_form':u_form,
        'p_form':p_form
    }
    return render(request, 'userapp/profile.html',context)