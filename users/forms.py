from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegister(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)

    #Meta is Used to Config Models And Fieldssssssssssssss.......

    class Meta:

        model = User
        fields = ['username','first_name','last_name','email','password1','password2']

class UserUpdate(forms.ModelForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)

    # Meta is Used to Config Models And Fieldssssssssssssss.......
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

class ProfileUpdate(forms.ModelForm):
    class Meta:
        model= Profile
        fields = ['image']