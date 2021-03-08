from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from .forms import UserCreationFormExtended, UserChangeFormExtended
from .models import Account, Profile


class CustomUserAdmin(UserAdmin):

    add_form = UserCreationFormExtended
    form = UserChangeFormExtended
    model = Account

    list_display = ['email','username','first_name','last_name','image','is_active','is_staff']
    search_fields = ['email','username',]
    readonly_fields = ['image']

    ordering = ()

    fieldsets = (
        (None, {'fields': ('password',)}),
        ('Personal information', {'fields': ('first_name', 'last_name', 'email', 'username', 'profile_image','image')}),
        ('Groups', {'fields': ('groups',)}),
        ('Permissions', {
            'fields': ('is_active','is_staff','is_superuser', 'user_permissions'),
        }),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
        #('Συνδρομή χρήστη', {'fields': ('end_of_subscription',)}),
    )

    add_fieldsets = (
        (None, {
            'fields': ('email', 'username', 'first_name', 'last_name', 'password1', 'password2'),
        }),
    )


admin.site.register(Account, CustomUserAdmin)
admin.site.register(Profile)

from . models import ArticlesViews, CoursesViews

admin.site.register(ArticlesViews)
admin.site.register(CoursesViews)



