from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django.contrib.auth.views import AuthenticationForm
from django.core.exceptions import ValidationError

from captcha.fields import ReCaptchaField



class UserCreationFormExtended(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')
    captcha = ReCaptchaField()

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


    def clean(self):
       username = self.cleaned_data.get('username')
       email = self.cleaned_data.get('email')
       if User.objects.filter(email=email).exists():
            raise ValidationError("Email already exists")
       if User.objects.filter(username=username).exists():
            raise ValidationError("Username already exists")

       return self.cleaned_data
