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
    comments = Comments.objects.filter(article=article)
    subcomments = SubComments.objects.filter(comment__article=article)

    if request.method == 'POST':

        comment_form = CommentsForm(request.POST)
        if comment_form.is_valid():
            comment_form.save()
            return redirect(reverse('article',args=[slug]) + '#footer')

        subcomment_form = SubCommentsForm(request.POST)
        if subcomment_form.is_valid():
            subcomment_form.save()
            return redirect(reverse('article',args=[slug]) + '#footer')

    comment_form = CommentsForm(initial={'article': article,'author':'Unknown'})
    subcomment_form = SubCommentsForm(initial={'author':'Unknown'})

    context = {'article':article, 'comments':comments, 'subcomments':subcomments, 'comment_form':comment_form, 'subcomment_form':subcomment_form}
    return render(request, 'articles/article.html', context)


def ajaxArticles(request):
    articles = Articles.objects.all()

    articles_Filter = ArticlesFilter(request.POST, queryset=articles)
    articles = articles_Filter.qs
    context ={'articles':articles}

    return render(request , 'articles/ajaxArticles.html', context)
