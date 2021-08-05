from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import userRegisterForm, userUpdateForm, profileUpdateForm
from django.contrib.auth.decorators import login_required

# Register view to register a new user
def register(request):

    # Check whether a request is post or not the work accordingly
    if request.method == "POST":
        form = userRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")

            # Sends a message to the template with this message
            messages.success(request,f"Account created with username {username}! Now login")

            # And redirect to the login url
            return redirect("login")
    else:
        form = userRegisterForm()
    
    # If form is not valid or request is not post the go to register page
    return render(request,"userapp/register.html",{"form":form})

# To update the profile
@login_required
def profile(request):
    if request.method == "POST":

        # Get data from both forms for username and password and profile photo
        u_form = userUpdateForm(request.POST, instance = request.user)
        p_form = profileUpdateForm(request.POST,request.FILES, instance = request.user.profile)
        
        # Check both forms validation and then save them to database and send a message to template
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
    # Render profile with new form data
    return render(request, 'userapp/profile.html',context)