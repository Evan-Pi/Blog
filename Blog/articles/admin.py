from django.contrib import admin
from . models import Articles, ArticlesCategories
from django_summernote.admin import SummernoteModelAdmin
from taggit.admin import Tag
#admin.site.site_header = 'My Site Admin Panel'
#admin.site.site_title = 'My Site Title'



class ArticlesAdmin(admin.ModelAdmin):
    
    def get_queryset(self, request):
        qs = super(ArticlesAdmin, self).get_queryset(request)

        if not request.user.is_superuser:
            filtered_qs = qs.filter(author=request.user)
        else:
            filtered_qs = qs

        return filtered_qs

    search_fields = ['title']
    list_display = ['title','image_tag','author','created','updated','publish_date']

class ArticlesCategoriesAdmin(admin.ModelAdmin):
    search_fields = ['title']


# Register your models here.
admin.site.register(Articles,ArticlesAdmin)
admin.site.register(ArticlesCategories,ArticlesCategoriesAdmin)






from django.contrib.admin.models import LogEntry

@admin.register(LogEntry)
class LogEntryAdmin(admin.ModelAdmin):
    # to have a date-based drilldown navigation in the admin page
    date_hierarchy = 'action_time'

    # to filter the resultes by users, content types and action flags
    list_filter = [
        'user',
        'content_type',
        'action_flag'
    ]

    # when searching the user will be able to search in both object_repr and change_message
    search_fields = [
        'object_repr',
        'change_message'
    ]

    list_display = [
        'action_time',
        'user',
        'content_type',
        'action_flag',
    ]