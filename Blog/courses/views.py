from django.shortcuts import render
from . models import CoursesCategories, Courses, Modules
from django.utils.timezone import localtime, now
from django.db.models import Q, Count
from django.core.paginator import Paginator
from users.models import Account, Profile, CoursesViews

# Create your views here.
def courses(request):
    current_datetime = localtime(now())
    categories = CoursesCategories.objects.annotate(courses_count=Count('courses', filter=Q(courses__publish_date__lte=current_datetime)))

    courses = Courses.objects.filter(publish_date__lte=current_datetime).order_by('-publish_date')

    #Pagination of courses
    paginator = Paginator(courses, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'categories':categories,'courses':courses,'page_obj':page_obj}
    return render(request, 'courses/courses.html', context)

from hitcount.views import HitCountDetailView

class Course(HitCountDetailView):
    model = Courses # your model goes here
    count_hit = True # set to True if you want it to try and count the hit
    template_name = 'courses/course.html'

    
    def get_object(self):
        obj = super().get_object()
        if self.request.user.is_authenticated:
            username = self.request.user.username
            user = Account.objects.get(username=username)
            profile = Profile.objects.get(user=user)
            CoursesViews.objects.create(course=obj, profile=profile)
        return obj
            

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        course = Courses.objects.get(slug=self.kwargs['slug'])
        modules = Modules.objects.filter(course=course)
        context['course'] = course
        context['modules'] = modules

        #Pagination of modules
        paginator = Paginator(modules, 1)
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context['page_obj'] = page_obj


        return context