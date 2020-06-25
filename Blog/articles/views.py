from django.shortcuts import render, redirect
from django.urls import reverse
from . models import Articles, ArticlesCategories
from . filters import ArticlesFilter
from django.utils.timezone import localtime, now
from django.db.models import Q, Count
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from users.models import Account, Profile, ArticlesViews

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

'''
def article(request, slug):
    article = Articles.objects.get(slug=slug)
    current_datetime = localtime(now())
    
    username = request.user.username
    if username != 'AnonymousUser' and username != '':
        user = Account.objects.get(username=username)
        profile = Profile.objects.get(user=user)
        ArticlesViews.objects.create(article=article, profile=profile)

    context = {'article':article, 'current_datetime':current_datetime}
    return render(request, 'articles/article.html', context)
'''

from hitcount.views import HitCountDetailView

class Article(HitCountDetailView):
    model = Articles # your model goes here
    count_hit = True # set to True if you want it to try and count the hit
    template_name = 'articles/article.html'

    
    def get_object(self):
        obj = super().get_object()
        if self.request.user.is_authenticated:
            username = self.request.user.username
            user = Account.objects.get(username=username)
            profile = Profile.objects.get(user=user)
            ArticlesViews.objects.create(article=obj, profile=profile)
        return obj
            

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        article = Articles.objects.get(slug=self.kwargs['slug'])
        context['article'] = article
        return context

    

           

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