from django.shortcuts import render, redirect
from . models import Discussions
from . forms import DiscussionForm
from . filters import DiscussionsFilter
from hitcount.views import HitCountDetailView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
import unicodedata
from django.contrib import messages

from users.models import Account, Profile, DiscussionViews

# Create your views here.
def forum(request):
    discussions = Discussions.objects.all().order_by('-created')
    login_form = AuthenticationForm()
    request_messages = messages.get_messages(request)

    if request.method == 'POST':
        create_discussion_form = DiscussionForm(request.POST)
        if create_discussion_form.is_valid():
            create_discussion_form.save()
            messages.success(request, 'Η συζήτηση δημιουργήθηκε!')
            return redirect('forum')


        

        mut = request.POST.copy()
        if 'search' in mut.keys():
            mut['search'] = ''.join(c for c in unicodedata.normalize('NFD', mut['search'].lower()) if unicodedata.category(c) != 'Mn')
            discussions_Filter = DiscussionsFilter(mut, queryset=discussions)
            discussions = discussions_Filter.qs
        else:
            discussions_Filter = DiscussionsFilter()

    else:
        create_discussion_form = DiscussionForm()
        discussions_Filter = DiscussionsFilter()

    context = {'discussions':discussions,'discussions_Filter':discussions_Filter, 'login_form':login_form, 'create_discussion_form':create_discussion_form, 'request_messages':request_messages}
    return render(request, 'forum/forum.html', context)


class discussion(HitCountDetailView):
    model = Discussions # your model goes here
    count_hit = True # set to True if you want it to try and count the hit
    template_name = 'forum/discussion.html'

    def get_object(self):
        obj = super().get_object()
        if self.request.user.is_authenticated:
            username = self.request.user.username
            user = Account.objects.get(username=username)
            profile = Profile.objects.get(user=user)
            DiscussionViews.objects.create(discussion=obj, profile=profile)

            qu = DiscussionViews.objects.filter(discussion=obj,profile=profile).order_by('-created')
            if len(qu)>1:
                qu[1].delete()
            
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        discussion = Discussions.objects.get(slug=self.kwargs['slug'],pk=self.kwargs['pk'])
        context['discussion'] = discussion
        return context

    