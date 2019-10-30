from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404,HttpResponseRedirect
import datetime as dt
from .models import Profile
from .forms import NewProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from rest_framework.response import Response
from rest_framework.views import APIView
# from .serializer import ProfileSerializer,ProjectSerializer
from rest_framework import status
from django.db.models import Max,F


@login_required(login_url='/accounts/login/')
def welcome(request):
    current_user = request.user


    return render(request,'users/index.html')

@login_required(login_url='/accounts/login/')
def user_profile(request):
    current_user = request.user
    # projects = Project.objects.filter(user=current_user).all()
    user_profile = Profile.objects.filter(user=current_user.id).first()
    

    return render(request, 'users/user_profile.html', { 'user_profile':user_profile})


@login_required(login_url='/accounts/login/')
def edit_profile(request):
    current_user = request.user
    
    if request.method == 'POST':
        form=NewProfileForm(request.POST, request.FILES)

        if form.is_valid():
            profile=form.save(commit=False)
            profile.user = current_user
            profile.save()

            return redirect('user-profile')

    else:
            form=NewProfileForm()

    return render(request, 'users/edit_profile.html', {'form':form,})







