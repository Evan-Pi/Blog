from django.contrib import admin
from . models import Articles, Comments, SubComments

# Register your models here.
admin.site.register(Articles)
admin.site.register(Comments)
admin.site.register(SubComments)
