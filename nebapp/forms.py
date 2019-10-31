from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Profile,Neighbourhood

class NewProfileForm(forms.ModelForm):
    class Meta:
        model= Profile
        fields = ['bio']
        exclude =['user']

class HoodForm(forms.ModelForm):
    class=Meta:
        model= Neighbourhood

