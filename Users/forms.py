
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegister(UserCreationForm):

    class Meta:
        model=User
        fields=['username','password1','password2']

class UserUpdate(forms.ModelForm):


    class Meta:
        model=User
        fields=['username']
