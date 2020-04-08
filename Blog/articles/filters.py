import django_filters
from django_filters import CharFilter
from django import forms
from . models import Articles

class ArticlesFilter(django_filters.FilterSet):

    title = CharFilter(field_name='title', lookup_expr='icontains', widget=forms.TextInput(attrs={'placeholder':'Search articles','id':'nav-tools-searchInput'}))

    class Meta:
        model = Articles
        fields = ['title']
