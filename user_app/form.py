from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField() # creating new field inside the form.

    class Meta:
        model = User  # validate which model to compare data with .
        fields = ["username", "email", "password1", "password2"]  
        # required fields, note: password2 => confirm password