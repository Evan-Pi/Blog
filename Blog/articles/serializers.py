from articles.models import Articles, ArticlesCategories
from rest_framework import routers, serializers, viewsets
from taggit_serializer.serializers import TagListSerializerField, TaggitSerializer
from django.utils.timezone import localtime, now


class ArticlesCategoriesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ArticlesCategories
        fields = '__all__'

class ArticlesCategoriesViewSet(viewsets.ModelViewSet):
    queryset = ArticlesCategories.objects.all()
    serializer_class = ArticlesCategoriesSerializer

class ArticlesSerializer(TaggitSerializer, serializers.HyperlinkedModelSerializer):

    tags = TagListSerializerField()

    class Meta:
        model = Articles
        fields = ['url','category','title','search','slug','subtitle','image','article', 'tags', 'created','updated','publish_date','author']

class ArticlesViewSet(viewsets.ModelViewSet):
    current_datetime = localtime(now())
    queryset = Articles.objects.filter(publish_date__lte=current_datetime).order_by('-publish_date')
    serializer_class = ArticlesSerializer