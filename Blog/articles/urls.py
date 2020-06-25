from django.conf import settings
from django.conf.urls.static import static

from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('privacy', views.privacy, name='privacy'),
    path('articles/', views.articles, name='articles'),
    path('articles/category/<str:slug>/', views.articlesCategory, name='articlesCategory'),
    path('articles/<str:slug>/', views.Article.as_view(), name='article'),
    path('authorsArticlesPreview', views.authorsArticlesPreview, name='authorsArticlesPreview'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)