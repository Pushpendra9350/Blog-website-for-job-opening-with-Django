from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import profile

# To make user registration forms 
class userRegisterForm(UserCreationForm):

    # Adding a new field 
    email = forms.EmailField()

    # class container with some options (metadata) attached to the model.
    class Meta:
        model = User
        fields = ["username","email","password1","password2"]

# Form to update a user profile username and email
class userUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    # Meta data for user model
    class Meta:
        model = User
        fields = ["username","email"]

# Profile photo update form for a user 
class profileUpdateForm(forms.ModelForm):
    class Meta:
        model = profile
        fields = ['image']
        