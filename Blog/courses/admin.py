from django.contrib import admin
from . models import CoursesCategories, Courses, Modules
# Register your models here.

class InLineModules(admin.StackedInline):
    model = Modules
    extra = 1

class CoursesAdmin(admin.ModelAdmin):
    inlines = [InLineModules]
    list_display = ('title','created','publish_date','author')
    list_filter = ('category',)
    search_fields = ('title',)

    class Media:
        css = {
            'all': ('courses/css/admin/styles.css',)
            }




admin.site.register(CoursesCategories)
admin.site.register(Courses,CoursesAdmin)
admin.site.register(Modules)
