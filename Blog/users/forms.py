from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django.contrib.auth.views import AuthenticationForm
from django.core.exceptions import ValidationError

from captcha.fields import ReCaptchaField

from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Account, Profile



class UserProfileImage(forms.ModelForm):
    profile_image = forms.ImageField(label='Profile image',required=False, error_messages = {'invalid':"Image files only"}, widget=forms.FileInput(attrs={'accept':'.png, .jpg, .jpeg'}))
    
    class Meta:
        model = Profile
        fields = ['profile_image']

        

class UserCreationFormExtended(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')
    captcha = ReCaptchaField()

    class Meta:
        model = Account
        fields = ('username', 'email', 'password1', 'password2')


    def __init__(self, *args, **kwargs):
        super(UserCreationFormExtended, self).__init__(*args, **kwargs)

        self.fields['username'].help_text = "150 χαρακτήρες ή λιγότεροι. Γράμματα, ψηφία και τα σύμβολα @/./+/-/_ μόνο."
        self.fields['email'].help_text = "Με αυτό το email θα συνδέεστε στον λογαριασμό σας."
        self.fields['password1'].help_text = "Τουλάχιστον 8 χαρακτήρες. Δεν μπορεί να περιέχει μόνο ψηφία. Αποφύγετε κοινότυπους κωδικούς και ομοιότητες με τις υπόλοιπες προσωπικές σας πληροφορίες."
        self.fields['password2'].help_text = "Εισάγετε τον ίδιο κωδικό για επαλήθευση"

        #self.fields['first_name'].help_text = "<span style='color:#44b78b;'>Προαιρετικό</span>"
        #self.fields['last_name'].help_text = "<span style='color:#44b78b;'>Προαιρετικό</span>"

        

        


class UserChangeFormExtended(UserChangeForm):

    class Meta:
        model = Account
        fields = ('username', 'email')