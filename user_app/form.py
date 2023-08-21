from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterForm(UserCreationForm):
    # creating new field inside the form.
    email = forms.EmailField() 
    # this is how we edit the default form attributes:
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields["username"].widget.attrs.update({
    #           "type":"text",
    #           "id":"FirstName",
    #           "name":"first_name",
    #           "class":"mt-1 w-[400px] rounded-md border-green-500 bg-yellow-300 text-sm text-gray-700 shadow-sm",
    #           "placeholder":"username",
    #     })
    # check out this video @ 1:33 
    # https://www.youtube.com/watch?v=t10QcFx7d5k&t=859s
    # https://github.com/flatplanet/Django-CRM
    # 
    class Meta:
        model = User  # validate which model to compare data with .
        fields = ["username", "email", "password1", "password2"]  
        # required fields, note: password2 => confirm password

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField() # creating new field inside the form.

    class Meta:
        model = User  # validate which model to compare data with .
        fields = ["username", "email"]  
        # required fields, username , email

class ProfileUpdateForm(forms.ModelForm):
        class Meta:
            model = Profile  # validate which model to compare data with .
            fields = ["image"]  
            # required fields, image