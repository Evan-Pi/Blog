from django.shortcuts import render, redirect
from django.urls import reverse
from . models import Articles, ArticlesCategories
from . filters import ArticlesFilter
from django.utils.timezone import localtime, now
from django.db.models import Q, Count

import unicodedata
# Create your views here.
def index(request):
    articles_Filter = ArticlesFilter()

    context = {'articles_Filter':articles_Filter}
    return render(request, 'articles/index.html', context)

def privacy(request):

    return render(request, 'articles/privacy.html')


def articles(request):
    current_datetime = localtime(now())
    categories = ArticlesCategories.objects.annotate(articles_count=Count('articles', filter=Q(articles__publish_date__lte=current_datetime)))
    
    articles = Articles.objects.filter(publish_date__lte=current_datetime).order_by('-publish_date')
    articles_Filter = ArticlesFilter(request.GET, queryset=articles)


    context = {'categories':categories, 'articles':articles, 'articles_Filter':articles_Filter}
    return render(request, 'articles/articles.html', context)

def article(request, slug):
    article = Articles.objects.get(slug=slug)
    articles_Filter = ArticlesFilter()
    current_datetime = localtime(now())

    context = {'article':article, 'articles_Filter':articles_Filter, 'current_datetime':current_datetime}
    return render(request, 'articles/article.html', context)

def articlesCategory(request, slug):
    category = ArticlesCategories.objects.get(slug=slug)
    current_datetime = localtime(now())
    articles = Articles.objects.filter(category=category,publish_date__lte=current_datetime).order_by('-publish_date')
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


def authorsArticlesPreview(request):
    current_datetime = localtime(now())
    articles = Articles.objects.filter(author=request.user).order_by('-publish_date')
    articles_Filter = ArticlesFilter(request.GET, queryset=articles)
    number_of_articles = len(articles)

    context = {'articles':articles, 'articles_Filter':articles_Filter, 'current_datetime':current_datetime, 'number_of_articles':number_of_articles}
    return render(request, 'articles/authorsArticlesPreview.html', context)

def ajaxAuthorsArticlesPreview(request):
    current_datetime = localtime(now())
    articles = Articles.objects.filter(author=request.user).order_by('-publish_date')

    mut = request.POST.copy()
    mut['search'] = ''.join(c for c in unicodedata.normalize('NFD', mut['search'].lower()) if unicodedata.category(c) != 'Mn')

    articles_Filter = ArticlesFilter(mut, queryset=articles)
    articles = articles_Filter.qs
    context ={'articles':articles}

    return render(request , 'articles/ajaxAuthorsArticlesPreview.html', context)