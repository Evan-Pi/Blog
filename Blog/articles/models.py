from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

from taggit.managers import TaggableManager
from django.utils.text import slugify
from unidecode import unidecode
import unicodedata

from django_currentuser.middleware import (get_current_user, get_current_authenticated_user)
from django_currentuser.db.models import CurrentUserField
# Create your models here.

class Articles(models.Model):
    '''Articles creation'''

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'

    title = models.CharField(max_length=256)
    slug = models.SlugField(editable=False,max_length=256)
    subtitle = models.CharField(max_length=256, blank=True)
    image = models.ImageField(upload_to = "Articles_Images", default='')
    article = RichTextUploadingField()

    tags = TaggableManager()

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    publish_date = models.DateTimeField()

    author = models.CharField(editable=False, default='', max_length=256)

    def save(self, *args, **kwargs):
        self.slug = slugify(unidecode(self.title))
        self.author = get_current_user().username
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
