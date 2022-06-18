from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Business,Profile

class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        
class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        fields = ['image','name','email','neighborhood']
        
class ProfileEdit(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image','username','email','neighborhood','bio']