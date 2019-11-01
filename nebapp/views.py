from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404,HttpResponseRedirect
import datetime as dt
from .models import Profile,Neighbourhood,Business,Post,Joining
from .forms import NewHoodForm,NewBusinessForm,NewPostForm
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

    else:
        hoods = Neighbourhood.objects.all()
        return render(request, 'users/index.html',{'hoods':hoods})


@login_required(login_url='/accounts/login/')
def user_profile(request, user_id):
    current_user = request.user
    title= "Profile"
    user_profile = Profile.objects.get(user_id=user_id)
    business = Business.objects.filter(user_id=user_id).all()
    hoods = Neighbourhood.objects.filter(user_id=user_id).all()
    users = User.objects.get(id=user_id)
    

    return render(request, 'users/user_profile.html', { 'user_profile':user_profile, 'hoods':hoods, 'business':business, 'users':users, 'title':title})


# @login_required(login_url='/accounts/login/')
# def edit_profile(request):
#     current_user = request.user
    
#     if request.method == 'POST':
#         form=NewProfileForm(request.POST, request.FILES)

#         if form.is_valid():
#             profile=form.save(commit=False)
#             profile.user = current_user
#             profile.save()

#             return redirect('user-profile')

#     else:
#             form=NewProfileForm()

#     return render(request, 'users/edit_profile.html', {'form':form,})


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


@login_required(login_url='/accounts/login/')
def create_hood(request):
    current_user = request.user
    if request.method =='POST':
        form = NewHoodForm(request.POST)
        if form.is_valid():
            hood = form.save(commit=False)
            hood.user = current_user
            hood.save()
            return redirect('welcome')

        else:
            form = NewHoodForm()
            return render(request, 'users/new_hood.html', {'form':form})

@login_required(login_url='/accounts/login/')
def update_hood(request, id):
    current_user = request.user
    neighbourhood = Neighbourhood.objects.get(pk=id)
    if request.method == 'POST':
        form = NewHoodForm(request.POST, instance = neighbourhood)
        if form.is_valid():
            hood = form.save(commit=False)
            hood.user = current_user
            hood.save()
            return redirect('welcome')

        else:
            form = NewHoodForm(instance=neighbourhood)
            return render(request, 'users/update_hood.html', {'form':form})


@login_required(login_url='/accounts/login/')
def delete_hood(request, id):
    Neighbourhood.objects.filter(pk=id).delete()
    return redirect('welcome')


@login_required(login_url='/accounts/login/')
def join(request, hoodid):
    current_user = request.user
    our_hood = Neighbourhood.objects.get(pk = hoodid)
    if Joining.objects.filter(user=current_user).exists():
        Joining.objects.filter(user_id=current_user).update(hood_id = our_hood.id)

    else:
        Joining(user=current_user, hood_id = our_hood.id).save()
    messages.success(request, "Thank you for joining the hood, Welcome in our hood!")
    return redirect('welcome')

@login_required(login_url='/accounts/login/')
def exit_hood(request, id):
    current_user = request.user
    Joining.objects.get(user_id = current_user).delete()
    messages.error(request, "You have exit the hood!")
    return redirect('welcome')

@login_required(login_url='/accounts/login/')
def add_bussiness(request):
    current_user = request.user
    hoods = Neighbourhood.objects.all()
    for hood in hoods:
        if Joining.objects.filter(user_id = request.user).exists():
            if request.method =='POST':
                form = NewBusinessForm(request.POST)
                if form.is_valid():
                    business = form.save(commit = False)
                    business.user = current_user
                    business.hood = hood
                    business.save()
                    messages.success(request, "Thank you for adding a business")
                    return redirect('welcome')

                else:
                    form = NewBusinessForm()
                    return render(request, 'users/business.html', {'form':form})

            else:
                messages.error(request, 'Sorry! You have to join the hood before creating a business')


@login_required(login_url='/accounts/login/')
def create_post(request):
    current_user = request.user
    hoods = Neighbourhood.objects.all()
    for hood in hoods:
        if Joining.objects.filter(user_id = current_user).exists():
            if request.method == 'POST':
                form = NewPostForm(request.POST)
                if form.is_valid():
                    post = form.save(commit=False)
                    post.user=current_user
                    post.hood = hood
                    post.save()
                    messages.success(request, 'You have added the post!')
                    return redirect('welcome')

                else:
                    form= NewPostForm()
                    return render(request, 'users/post.html', {'form':form})

            else:
                messages.error(request, 'sorry!!You have to create a post when you have joined the hood!')








