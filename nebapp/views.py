from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404,HttpResponseRedirect
import datetime as dt
from .models import Profile,Neighbourhood,Business,Post,Joining
from .forms import NewProfileForm,HoodForm,NewBusinessForm,NewPostForm
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
    if Joining.objects.filter(user_id=current_user).exists():
        hoods = Neighbourhood.objects.get(pk=current_user.join.hood_id)
        members = Profile.get_user_by_hood(id= current_user.join.hood_id).all()
        posts = Post.get_post_by_hood(id=current_user.join.hood_id)
        business = Business.get_businesses(id= current_user.join.hood_id)

    return render(request,'users/index.html', {'hoods':hoods, 'members':members, 'posts':posts, 'business':business})

@login_required(login_url='/accounts/login/')
def user_profile(request, user_id):
    current_user = request.user
    title= "Profile"
    user_profile = Profile.objects.get(user_id=user_id)
    business = Business.objects.filter(user_id=user_id).all()
    hoods = Neighbourhood.objects.filter(user_id=user_id).all()
    users = User.objects.get(id=user_id)
    

    return render(request, 'users/user_profile.html', { 'user_profile':user_profile, 'hoods':hoods, 'business':business, 'users':users, 'title':title})


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
    if 'hood' in request.GET and request.GET['hood']:
        search_term= request.GET.get('hood')
        searched_hoods=Neighbourhood.search_by_title(search_term)
        message=f'{search_term}'

        return render(request,'users/search.html',{'message':message,'hood':searched_hoods})

    else:
        message="You haven't searched for any neighbourhood"
        return render(request, 'users/search.html',{'message':message})










