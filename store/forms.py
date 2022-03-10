from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms.models import ModelForm



class CreateUserForm(UserCreationForm):
    """
    This class is used to create the registration form
    """
    class Meta:
        model= User
        fields= ['username', 'email', 'password1', 'password2']