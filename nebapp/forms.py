from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Profile

class NewProfileForm(forms.ModelForm):
    class Meta:
        model= Profile
        exclude =['user']
