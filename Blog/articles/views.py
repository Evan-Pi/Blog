from django.shortcuts import render, redirect
from django.urls import reverse
from . models import Articles, ArticlesCategories
from . filters import ArticlesFilter
from django.utils.timezone import localtime, now
from django.db.models import Q, Count
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

import unicodedata
from django.contrib.auth.decorators import user_passes_test

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

    if request.method == 'POST':
        mut = request.POST.copy()
        mut['search'] = ''.join(c for c in unicodedata.normalize('NFD', mut['search'].lower()) if unicodedata.category(c) != 'Mn')
        articles_Filter = ArticlesFilter(mut, queryset=articles)
        
        articles = articles_Filter.qs
    else:
        articles_Filter = ArticlesFilter()

    #Pagination of articles
    paginator = Paginator(articles, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'categories':categories,'articles':articles,'page_obj':page_obj,'articles_Filter':articles_Filter}
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

    if request.method == 'POST':
        mut = request.POST.copy()
        mut['search'] = ''.join(c for c in unicodedata.normalize('NFD', mut['search'].lower()) if unicodedata.category(c) != 'Mn')
        articles_Filter = ArticlesFilter(mut, queryset=articles)
        articles = articles_Filter.qs
    else:
        articles_Filter = ArticlesFilter()
 
    #Pagination of articles
    paginator = Paginator(articles, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)


    context = {'category':category,'articles':articles,'page_obj':page_obj, 'articles_Filter':articles_Filter}
    return render(request, 'articles/articlesCategory.html', context)

@user_passes_test(lambda u: u.is_superuser or u.is_staff)
def authorsArticlesPreview(request):
    current_datetime = localtime(now())
    articles = Articles.objects.filter(author=request.user).order_by('-publish_date')

    if request.method == 'POST':
        mut = request.POST.copy()
        mut['search'] = ''.join(c for c in unicodedata.normalize('NFD', mut['search'].lower()) if unicodedata.category(c) != 'Mn')
        articles_Filter = ArticlesFilter(mut, queryset=articles)
        articles = articles_Filter.qs
    else:
        articles_Filter = ArticlesFilter()
        
    number_of_articles = len(articles)

    #Pagination of articles
    paginator = Paginator(articles, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'articles':articles, 'articles_Filter':articles_Filter,'page_obj':page_obj, 'current_datetime':current_datetime, 'number_of_articles':number_of_articles}
    return render(request, 'articles/authorsArticlesPreview.html', context)