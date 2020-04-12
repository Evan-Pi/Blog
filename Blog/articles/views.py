from django.shortcuts import render, redirect
from django.urls import reverse
from . models import Articles, ArticlesCategories
from . filters import ArticlesFilter
from django.utils.timezone import localtime, now

import unicodedata
# Create your views here.
def index(request):
    articles_Filter = ArticlesFilter()

    context = {'articles_Filter':articles_Filter}
    return render(request, 'articles/index.html', context)

def articles(request):
    categories = ArticlesCategories.objects.all()
    current_datetime = localtime(now())
    articles = Articles.objects.filter(publish_date__lte=current_datetime).order_by('-publish_date')
    articles_Filter = ArticlesFilter(request.GET, queryset=articles)


    context = {'categories':categories, 'articles':articles, 'articles_Filter':articles_Filter}
    return render(request, 'articles/articles.html', context)

def article(request, slug):
    article = Articles.objects.get(slug=slug)
    articles_Filter = ArticlesFilter()

    context = {'article':article, 'articles_Filter':articles_Filter}
    return render(request, 'articles/article.html', context)

def articlesCategory(request, slug):
    category = ArticlesCategories.objects.get(slug=slug)
    articles = Articles.objects.filter(category=category)
    articles_Filter = ArticlesFilter()


    context = {'category':category,'articles':articles, 'articles_Filter':articles_Filter}
    return render(request, 'articles/articlesCategory.html', context)


def ajaxArticles(request):
    current_datetime = localtime(now())
    articles = Articles.objects.filter(publish_date__lte=current_datetime).order_by('-publish_date')

    mut = request.POST.copy()
    mut['search'] = ''.join(c for c in unicodedata.normalize('NFD', mut['search'].lower()) if unicodedata.category(c) != 'Mn')

    articles_Filter = ArticlesFilter(mut, queryset=articles)
    articles = articles_Filter.qs
    context ={'articles':articles}

    return render(request , 'articles/ajaxArticles.html', context)

def ajaxCategoryArticles(request,slug):
    category = ArticlesCategories.objects.get(slug=slug)
    current_datetime = localtime(now())
    articles = Articles.objects.filter(publish_date__lte=current_datetime, category__slug=slug).order_by('-publish_date')

    mut = request.POST.copy()
    mut['search'] = ''.join(c for c in unicodedata.normalize('NFD', mut['search'].lower()) if unicodedata.category(c) != 'Mn')

    articles_Filter = ArticlesFilter(mut, queryset=articles)
    articles = articles_Filter.qs
    context ={'category':category,'articles':articles}

    return render(request , 'articles/ajaxCategoryArticles.html', context)
