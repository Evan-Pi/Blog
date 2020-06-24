from articles.models import Articles, ArticlesCategories
from rest_framework import routers, serializers, viewsets
from taggit_serializer.serializers import TagListSerializerField, TaggitSerializer


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
    queryset = Articles.objects.all()
    serializer_class = ArticlesSerializer