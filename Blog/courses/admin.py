from django.contrib import admin
from . models import CoursesCategories, Courses, Modules
# Register your models here.

class InLineModules(admin.StackedInline):
    model = Modules
    extra = 1

class CoursesAdmin(admin.ModelAdmin):

    def get_queryset(self, request):
        qs = super(CoursesAdmin, self).get_queryset(request)

        if not request.user.is_superuser:
            filtered_qs = qs.filter(author=request.user)
        else:
            filtered_qs = qs

        return filtered_qs

    inlines = [InLineModules]
    list_display = ('title','image_tag','created','publish_date','author')
    list_filter = ('category',)
    search_fields = ('title',)

    class Media:
        css = {
            'all': ('courses/css/admin/styles.css',)
            }


admin.site.register(CoursesCategories)
admin.site.register(Courses,CoursesAdmin)

