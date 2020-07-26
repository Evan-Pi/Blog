from django.shortcuts import render, redirect
#from django.contrib.auth.forms import UserCreationForm
from . forms import UserCreationFormExtended
from django.contrib.auth.models import Group
from . forms import UserProfileImage
from . models import Account, Profile, ArticlesViews, CoursesViews, DiscussionViews

from django.contrib.auth.decorators import login_required


from django.contrib.auth import authenticate, login
from django.contrib import messages

# Create your views here.
def signup(request):

    if request.method == 'POST':
        form = UserCreationFormExtended(request.POST)
        if form.is_valid():
            user = form.save()
            members, created = Group.objects.get_or_create(name='Members')
            members.user_set.add(user)

            
            new_user = authenticate(email=form.cleaned_data['email'], password=form.cleaned_data['password1'])
            login(request, new_user)

            messages.success(request, 'Ο λογαριασμός σου δημιουργήθηκε με επιτυχία! Καλώς ήρθες στην κοινότητα του Φοίνικα!')
            return redirect('profile')
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

    viewed_articles = ArticlesViews.objects.filter(profile=profile).order_by('-created')[:4]
    viewed_courses = CoursesViews.objects.filter(profile=profile).order_by('-created')[:4]
    viewed_discussions = DiscussionViews.objects.filter(profile=profile).order_by('-created')[:4]

    if request.method == "POST": 
        form = UserProfileImage(request.POST, request.FILES, instance=request.user.profile) 
        if form.is_valid(): 
            form.save() 
            return redirect('profile')
    else: 
        form = UserProfileImage(instance=request.user.profile)
        
    context = {'form':form, 'profile':profile, 'viewed_articles':viewed_articles, 'viewed_courses':viewed_courses , 'viewed_discussions':viewed_discussions}
    return render(request, 'users/profile.html', context)
