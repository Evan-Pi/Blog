from django.shortcuts import render, redirect
#from django.contrib.auth.forms import UserCreationForm
from . forms import UserCreationFormExtended
from django.contrib.auth.models import Group
from . forms import UserProfileImage
from . models import Account, Profile, ArticlesViews
import numpy as np

from django.contrib.auth.decorators import login_required

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = UserCreationFormExtended(request.POST)
        if form.is_valid():
            user = form.save()
            members, created = Group.objects.get_or_create(name='Members')
            members.user_set.add(user)
            return redirect('signup_success')
    else:
        form = UserCreationFormExtended()

    context = {'form':form}
    return render(request, 'registration/signup.html', context)

def signup_success(request):
    return render(request, 'registration/signup_success.html')



@login_required
def profile(request):
    username = request.user.username
    profile = Profile.objects.get(user__username=username)
    viewed_articles_all = ArticlesViews.objects.filter(profile=profile).order_by('-created')
    
    unique_titles = list(np.unique([i.article.title for i in viewed_articles_all]))
    viewed_articles = []
    for i in viewed_articles_all:
        if i.article.title in unique_titles:
            viewed_articles.append(i)
            unique_titles.remove(i.article.title)
    viewed_articles = viewed_articles[:4]

    if request.method == "POST": 
        form = UserProfileImage(request.POST, request.FILES, instance=request.user.profile) 
        if form.is_valid(): 
            form.save() 
            return redirect('profile')
    else: 
        form = UserProfileImage(instance=request.user.profile)
        
    context = {'form':form, 'profile':profile, 'viewed_articles':viewed_articles}
    return render(request, 'users/profile.html', context)
