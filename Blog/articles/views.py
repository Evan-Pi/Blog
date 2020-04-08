from django.shortcuts import render, redirect
from django.urls import reverse
from . models import Articles, Comments, SubComments
from . forms import CommentsForm, SubCommentsForm
from . filters import ArticlesFilter
# Create your views here.
def index(request):
    articles = Articles.objects.all()
    articles_Filter = ArticlesFilter(request.GET, queryset=articles)

    context = {'articles':articles, 'articles_Filter':articles_Filter}
    return render(request, 'articles/index.html', context)

def articles(request):
    articles = Articles.objects.all()
    articles_Filter = ArticlesFilter(request.GET, queryset=articles)

    context = {'articles':articles, 'articles_Filter':articles_Filter}
    return render(request, 'articles/articles.html', context)

def article(request, slug):
    article = Articles.objects.get(slug=slug)
    articles = Articles.objects.all()
    articles_Filter = ArticlesFilter(request.GET, queryset=articles)

    context = {'article':article, 'articles_Filter':articles_Filter}
    return render(request, 'articles/article.html', context)


def ajaxArticles(request):
    articles = Articles.objects.all()

    articles_Filter = ArticlesFilter(request.POST, queryset=articles)
    articles = articles_Filter.qs
    context ={'articles':articles}

    return render(request , 'articles/ajaxArticles.html', context)
