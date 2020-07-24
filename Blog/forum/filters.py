import django_filters
from django_filters import CharFilter
from django import forms
from . models import Discussions

class DiscussionsFilter(django_filters.FilterSet):

    search = CharFilter(field_name='search', lookup_expr='icontains', widget=forms.TextInput(attrs={'class':'form-control','placeholder':"Αναζήτηση συζητήσεων",'id':'discussions-search-input'}))
    class Meta:
        model = Discussions
        fields = ['search']