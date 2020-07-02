from django.urls import path, include
from . import views

urlpatterns = [
    path('courses/', views.courses, name='courses'),
    path('courses/<str:slug>/', views.Course.as_view(), name='course'),
    path('courses/category/<str:slug>/', views.coursesCategory, name='coursesCategory'),
]