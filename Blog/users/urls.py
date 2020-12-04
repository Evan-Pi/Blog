from django.urls import path
from . import views

from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('login_success', views.login_success, name='login_success'),
    path('signup', views.signup, name='signup'),
    path('profile/', views.profile, name='profile'),
]
