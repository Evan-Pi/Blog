from django.contrib import admin
from . models import Articles, ArticlesCategories

# Register your models here.
admin.site.register(Articles)
admin.site.register(ArticlesCategories)
