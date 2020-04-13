from django.urls import path
from . import views


urlpatterns = [
    path('signup', views.signup, name='signup'),
    path('signup_success', views.signup_success, name='signup_success'),
    
    path('profile/', views.profile, name='profile'),
]
