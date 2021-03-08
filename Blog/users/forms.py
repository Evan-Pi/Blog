from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Account

class UserCreationFormExtended(UserCreationForm):
    class Meta:
        model = Account
        fields = ('email', 'username', 'password1', 'password2')
        
    email = forms.EmailField(max_length=200)

class UserChangeFormExtended(UserChangeForm):

    class Meta:
        model = Account
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(UserChangeFormExtended, self).__init__(*args, **kwargs)

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model=Account
        fields=['profile_image','first_name','last_name']

    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'First name'}),required=False)
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Last name'}),required=False)
    profile_image = forms.ImageField(widget=forms.FileInput(),required=False)
 