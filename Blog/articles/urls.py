from django.conf import settings
from django.conf.urls.static import static

from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.index, name='index'),
    path('privacy', views.privacy, name='privacy'),
    path('informations', views.informations, name='informations'),
    path('articles/', views.articles, name='articles'),
    path('articles/category/<str:slug>/', views.articlesCategory, name='articlesCategory'),


    path('articles/<str:slug>/', views.Article.as_view(), name='article'),
    path('ajax_comments/<str:slug>/', views.ajax_comments, name='ajax_comments'),

    path('articles/edit/<str:slug>/', views.edit_article, name='edit_article'),

    path('authorsArticlesPreview', views.authorsArticlesPreview, name='authorsArticlesPreview'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)