from django.shortcuts import render, redirect
from . models import Account, Profile, ArticlesViews, CoursesViews
from . forms import UserCreationFormExtended
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib import messages

def login_success(request):
    return redirect("profile")

# Create your views here.
def signup(request):

    if request.method == 'POST':
        form = UserCreationFormExtended(request.POST)
        if form.is_valid():
            user = form.save()
            new_user = authenticate(email=form.cleaned_data['email'], password=form.cleaned_data['password1'])
            login(request, new_user)
            messages.success(request, 'Account created successfully!')
            return redirect('profile')
    else:
        form = UserCreationFormExtended()

    context = {'form':form}
    return render(request, 'registration/signup.html', context)

def signup_success(request):
    return render(request, 'registration/signup_success.html')

@login_required
def profile(request):

    profile = Profile.objects.get(user__email=request.user.email)

    viewed_articles = ArticlesViews.objects.filter(profile=profile).order_by('-created')[:4]
    viewed_courses = CoursesViews.objects.filter(profile=profile).order_by('-created')[:4]
        
    context = {'profile':profile, 'viewed_articles':viewed_articles, 'viewed_courses':viewed_courses}
    return render(request, 'users/profile.html', context)