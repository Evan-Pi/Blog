from django.conf import settings
from django.conf.urls.static import static

from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('articles/', views.articles, name='articles'),
    path('articles/<str:slug>/', views.article, name='article'),

    path('ajaxArticles', views.ajaxArticles, name='ajaxArticles'),

    #path('ajaxComments/<str:slug>/', views.ajaxComments, name='ajaxComments'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)