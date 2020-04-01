from django.shortcuts import render, redirect
from . models import Articles, Comments, SubComments
from . forms import CommentsForm
# Create your views here.
def index(request):
    articles = Articles.objects.all()

    context = {'articles':articles}
    return render(request, 'articles/index.html', context)

def article(request, slug):
    article = Articles.objects.get(slug=slug)
    comments = Comments.objects.filter(article=article)
    subcomments = SubComments.objects.filter(comment__article=article)


    comment_form = CommentsForm(initial={'article': article})
    if request.method == 'POST':
        comment_form = CommentsForm(request.POST)
        if comment_form.is_valid():
            comment_form.save()
            return redirect('article', slug=article.slug)

    context = {'article':article, 'comments':comments, 'subcomments':subcomments, 'comment_form':comment_form}
    return render(request, 'articles/article.html', context)
