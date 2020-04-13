from django.shortcuts import render, redirect
#from django.contrib.auth.forms import UserCreationForm
from . forms import UserCreationFormExtended
from django.contrib.auth.models import Group

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = UserCreationFormExtended(request.POST)
        if form.is_valid():
            user = form.save()
            visitors = Group.objects.get(name='Visitors')
            visitors.user_set.add(user)
            return redirect('signup_success')
    else:
        form = UserCreationFormExtended()

    context = {'form':form}
    return render(request, 'registration/signup.html', context)

def signup_success(request):
    return render(request, 'registration/signup_success.html')

def profile(request):
    return render(request, 'users/profile.html')
