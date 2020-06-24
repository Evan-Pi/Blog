from django.contrib import admin

# Register your models here.
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import UserCreationFormExtended, UserChangeFormExtended
from .models import Account, Profile

class CustomUserAdmin(UserAdmin):
    add_form = UserCreationFormExtended
    form = UserChangeFormExtended
    model = Account
    list_display = [ 'username', 'email', 'first_name', 'last_name', 'date_joined', 'last_login', 'is_staff']

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'captcha'),
        }),
    )
    


admin.site.register(Account, CustomUserAdmin)
admin.site.register(Profile)

