from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.forum, name='forum'),
    path('discussion/<str:slug>/<str:pk>/', views.discussion.as_view(), name='discussion'),
]