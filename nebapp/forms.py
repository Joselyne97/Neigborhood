from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Neighbourhood,Post,Business

# class NewProfileForm(forms.ModelForm):
#     class Meta:
#         model= Profile
#         fields = ['bio']
#         exclude =['user']

class NewHoodForm(forms.ModelForm):
    class Meta:
        model= Neighbourhood
        fields = ['name','description','location','police_contact','hospital_contact']
        exclude =['user']

class NewBusinessForm(forms.ModelForm):
    class Meta:
        model= Business
        exclude=['user','hood']

class NewPostForm(forms.ModelForm):
    class Meta:
        model= Post
        exclude=['user','hood']


