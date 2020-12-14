from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from articles.serializers import ArticlesCategoriesViewSet, ArticlesViewSet


router = routers.DefaultRouter()
router.register('articles-categories', ArticlesCategoriesViewSet)
router.register('articles', ArticlesViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    path('admin/', admin.site.urls),

    path('', include('articles.urls')),
    path('', include('courses.urls')),

    path('summernote/', include('django_summernote.urls')),

    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('users.urls')),
]
