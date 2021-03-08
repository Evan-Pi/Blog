from django.shortcuts import render, redirect
from django.urls import reverse
from . models import Articles, ArticlesCategories, Comments, SubComments
from courses.models import Courses, CoursesCategories
from . filters import ArticlesFilter
from django.utils.timezone import localtime, now
from django.db.models import Q, Count
from django.core.paginator import Paginator

from users.models import Account, Profile, ArticlesViews

import unicodedata
from django.contrib.auth.decorators import user_passes_test

from . forms import EditArticleForm, CommentsForm, SubCommentsForm
from django.http import HttpResponseRedirect


def coming_soon(request):

    return render(request, 'articles/coming_soon.html')

def index(request):
    current_datetime = localtime(now())

    current_datetime = localtime(now())
    articles_categories = ArticlesCategories.objects.annotate(articles_count=Count('articles', filter=Q(articles__publish_date__lte=current_datetime)))
    courses_categories = CoursesCategories.objects.annotate(courses_count=Count('courses', filter=Q(courses__publish_date__lte=current_datetime)))

    recent_articles = Articles.objects.filter(publish_date__lte=current_datetime).order_by('-publish_date')[:4]
    popular_courses = Courses.objects.filter(publish_date__lte=current_datetime).order_by('-hit_count_generic__hits')[:4]

    context = {'recent_articles':recent_articles, 'popular_courses':popular_courses, 'articles_categories':articles_categories,'courses_categories':courses_categories}
    return render(request, 'articles/index.html', context)

def privacy(request):

    return render(request, 'articles/privacy.html')

def informations(request):

    return render(request, 'articles/informations.html')


def articles(request):
    current_datetime = localtime(now())
    categories = ArticlesCategories.objects.annotate(articles_count=Count('articles', filter=Q(articles__publish_date__lte=current_datetime)))

    articles = Articles.objects.filter(publish_date__lte=current_datetime,approved=True).order_by('-publish_date')

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

from hitcount.views import HitCountDetailView

class Article(HitCountDetailView):
    model = Articles # your model goes here
    count_hit = True # set to True if you want it to try and count the hit
    template_name = 'articles/article.html'

    def get_object(self):
        obj = super().get_object()
        if self.request.user.is_authenticated:
            profile = Profile.objects.get(user=self.request.user)
            ArticlesViews.objects.create(article=obj, profile=profile)
            qu = ArticlesViews.objects.filter(article=obj,profile=profile).order_by('-created')
            if len(qu)>1:
                qu[1].delete()
        return obj
    
    def get_context_data(self, **kwargs):
        context = super(Article, self).get_context_data(**kwargs)
        article = kwargs['object']        
        current_datetime = localtime(now())
        if (article.publish_date > current_datetime or article.approved == False) and (article.author != self.request.user.username) and not (self.request.user.is_superuser):
            not_approved_article = True
        else:
            not_approved_article = False
        context['article'] = article
        context['not_approved_article'] = not_approved_article
        return context

    


        

def ajax_comments(request, slug):

    article = Articles.objects.get(slug=slug)

    comments_form = CommentsForm(request.POST)
    if comments_form.is_valid():
        comments_form.save()

    subcomments_form = SubCommentsForm(request.POST)
    if subcomments_form.is_valid():
        subcomments_form.save()

    comments = Comments.objects.filter(article=article).order_by('-created_date')
    subcomments = SubComments.objects.filter(comment__article=article).order_by('-created_date')
    comments_form =  CommentsForm(initial={'article':article, 'author':request.user})
    subcomments_form = SubCommentsForm(initial={'author':request.user})


    context = {'comments':comments, 'subcomments':subcomments,'comments_form':comments_form, 'subcomments_form':subcomments_form}    

    return render(request, 'articles/comments/ajaxComments.html', context)



    
def edit_article(request, slug):
    article = Articles.objects.get(slug=slug)
    form = EditArticleForm(instance=article)
    context={'article':article, 'form':form}
    return render(request, 'articles/edit_article.html', context)
           

def articlesCategory(request, slug):
    category = ArticlesCategories.objects.get(slug=slug)
    current_datetime = localtime(now())
    articles = Articles.objects.filter(category=category,publish_date__lte=current_datetime,approved=True).order_by('-publish_date')

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