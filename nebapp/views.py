from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404,HttpResponseRedirect
import datetime as dt
from .models import Profile,Neighbourhood
from .forms import NewProfileForm,HoodForm
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
    neighbourhoods=Neighbourhood.objects.all()

    return render(request,'users/index.html',locals())

@login_required(login_url='/accounts/login/')
def user_profile(request):
    current_user = request.user
    user_profile = Profile.objects.get(user=request.user)
    

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


@login_required(login_url='/accounts/login/')
def search_results(request):
    if 'neighbourhood' in request.GET and request.GET['neighbourhood']:
        search_term= request.GET.get('neighbourhood')
        searched_neighbourhoods=Neighbourhood.search_by_title(search_term)
        message=f'{search_term}'

        return render(request,'users/search.html',{'message':message,'neighbourhoods':searched_neighbourhoods})

    else:
        message="You haven't searched for any neighbourhood"
        return render(request, 'users/search.html',{'message':message})










