from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django.contrib.auth.views import AuthenticationForm
from django.core.exceptions import ValidationError

from captcha.fields import ReCaptchaField

from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Account, Profile



class UserProfileImage(forms.ModelForm):
    profile_image = forms.ImageField(label='Profile image',required=False, error_messages = {'invalid':"Image files only"}, widget=forms.FileInput)
    class Meta:
        model = Profile
        fields = ['profile_image']

        

class UserCreationFormExtended(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')
    captcha = ReCaptchaField()

    class Meta:
        model = Account
        fields = ('username', 'email', 'password1', 'password2')


    def clean(self):
       username = self.cleaned_data.get('username')
       email = self.cleaned_data.get('email')
       if Account.objects.filter(email=email).exists():
            raise ValidationError("Email already exists")
       if Account.objects.filter(username=username).exists():
            raise ValidationError("Username already exists")

       return self.cleaned_data

class UserChangeFormExtended(UserChangeForm):

    class Meta:
        model = Account
        fields = ('username', 'email')