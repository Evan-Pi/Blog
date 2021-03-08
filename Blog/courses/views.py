from django.shortcuts import render
from . models import CoursesCategories, Courses, Modules
from django.utils.timezone import localtime, now
from django.db.models import Q, Count
from django.core.paginator import Paginator
from users.models import Account, Profile, CoursesViews
from hitcount.views import HitCountDetailView
from . filters import CoursesFilter

import unicodedata
from django.contrib.auth.decorators import user_passes_test

# Create your views here.
def courses(request):
    current_datetime = localtime(now())
    categories = CoursesCategories.objects.annotate(courses_count=Count('courses', filter=Q(courses__publish_date__lte=current_datetime)))

    courses = Courses.objects.filter(publish_date__lte=current_datetime,approved=True).order_by('-publish_date')

    if request.method == 'POST':
        mut = request.POST.copy()
        mut['search'] = ''.join(c for c in unicodedata.normalize('NFD', mut['search'].lower()) if unicodedata.category(c) != 'Mn')
        courses_Filter = CoursesFilter(mut, queryset=courses)
        
        courses = courses_Filter.qs
    else:
        courses_Filter = CoursesFilter()

    #Pagination of courses
    paginator = Paginator(courses, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'categories':categories,'courses':courses,'page_obj':page_obj,'courses_Filter':courses_Filter}
    return render(request, 'courses/courses.html', context)

def coursesCategory(request, slug):
    category = CoursesCategories.objects.get(slug=slug)
    current_datetime = localtime(now())
    courses = Courses.objects.filter(category=category,publish_date__lte=current_datetime,approved=True).order_by('-publish_date')

    if request.method == 'POST':
        mut = request.POST.copy()
        mut['search'] = ''.join(c for c in unicodedata.normalize('NFD', mut['search'].lower()) if unicodedata.category(c) != 'Mn')
        courses_Filter = CoursesFilter(mut, queryset=courses)
        courses = courses_Filter.qs
    else:
        courses_Filter = CoursesFilter()
 
    #Pagination of courses
    paginator = Paginator(courses, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)


    context = {'category':category,'courses':courses,'page_obj':page_obj, 'courses_Filter':courses_Filter}
    return render(request, 'courses/coursesCategory.html', context)

class Course(HitCountDetailView):
    model = Courses # your model goes here
    count_hit = True # set to True if you want it to try and count the hit
    template_name = 'courses/course.html'

    
    def get_object(self):
        obj = super().get_object()
        if self.request.user.is_authenticated:
            profile = Profile.objects.get(user=self.request.user)
            CoursesViews.objects.create(course=obj, profile=profile)
            qu = CoursesViews.objects.filter(course=obj,profile=profile).order_by('-created')
            if len(qu)>1:
                qu[1].delete()
        return obj
            

    def get_context_data(self, **kwargs):
        context = super(Course, self).get_context_data(**kwargs)
        current_datetime = localtime(now())
        course = kwargs['object']
        modules = Modules.objects.filter(course=course).order_by('order')

        #Pagination of modules
        paginator = Paginator(modules, 1)
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        if (course.publish_date > current_datetime or course.approved == False) and (course.author.email != self.request.user.email) and not (self.request.user.is_superuser) :
            not_approved_course = True
        else:
            not_approved_course = False

        context['course'] = course
        context['modules'] = modules
        context['page_obj'] = page_obj
        context['not_approved_course'] = not_approved_course

        return context


@user_passes_test(lambda u: u.is_superuser or u.is_staff)
def authorsCoursesPreview(request):
    current_datetime = localtime(now())
    courses = Courses.objects.filter(author=request.user).order_by('-publish_date')
    
    if request.method == 'POST':
        mut = request.POST.copy()
        mut['search'] = ''.join(c for c in unicodedata.normalize('NFD', mut['search'].lower()) if unicodedata.category(c) != 'Mn')
        courses_Filter = CoursesFilter(mut, queryset=courses)
        courses = courses_Filter.qs
    else:
        courses_Filter = CoursesFilter()
        
    number_of_courses = len(courses)

    #Pagination of courses
    paginator = Paginator(courses, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'courses':courses, 'courses_Filter':courses_Filter,'page_obj':page_obj, 'current_datetime':current_datetime, 'number_of_courses':number_of_courses}
    return render(request, 'courses/authorsCoursesPreview.html', context)