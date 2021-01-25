from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserCreate(UserCreationForm):

    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class ProfileUpdate(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username','email']

class ProfileImageUpdate(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['image']