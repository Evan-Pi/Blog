from django.contrib import admin
from . models import Discussions
# Register your models here.

class DiscussionsAdmin(admin.ModelAdmin):
    
    def get_queryset(self, request):
        qs = super(DiscussionsAdmin, self).get_queryset(request)

        if not request.user.is_superuser:
            filtered_qs = qs.filter(author=request.user)
        else:
            filtered_qs = qs

        return filtered_qs

    search_fields = ['title']
    list_display = ['title','created','author']

admin.site.register(Discussions)
