from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

from taggit.managers import TaggableManager
from django.utils.text import slugify
from unidecode import unidecode
import unicodedata

from django_currentuser.middleware import (get_current_user, get_current_authenticated_user)
from django_currentuser.db.models import CurrentUserField

from django.urls import reverse
from django.contrib.contenttypes.models import ContentType

from hitcount.models import HitCount, HitCountMixin

class CoursesCategories(models.Model):
    '''Courses categories creation'''

    class Meta:
        verbose_name = 'Course Category'
        verbose_name_plural = 'Courses Categories'

    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(editable=False,max_length=100,default='')
    image = models.ImageField(upload_to = "Courses_Categories_Images", default='', blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(unidecode(self.title))
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Courses(models.Model, HitCountMixin):
    '''Courses creation'''

    class Meta:
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'

    category = models.ForeignKey(CoursesCategories, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=256,unique=True)
    search = models.CharField(default='',editable=False,max_length=512)
    slug = models.SlugField(editable=False,max_length=256)
    subtitle = models.CharField(max_length=256, blank=True)
    image = models.ImageField(upload_to = "Courses_Images", default='')
    use_image_as_background_in_course = models.BooleanField(default=True)

    tags = TaggableManager(blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    publish_date = models.DateTimeField()


    author = models.CharField(editable=False, default='', max_length=256)

    def save(self, *args, **kwargs):
        self.slug = slugify(unidecode(self.title))
        self.author = get_current_user().username
        self.search = ''.join(c for c in unicodedata.normalize('NFD', self.title.lower() + ' ' + self.subtitle.lower() + self.author.lower() ) if unicodedata.category(c) != 'Mn')
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('course', args=[self.slug])

    def get_admin_url(self):
        content_type = ContentType.objects.get_for_model(self.__class__)
        return reverse("admin:%s_%s_change" % (content_type.app_label, content_type.model), args=(self.id,))

    def __str__(self):
        return f'{self.category.title} - {self.title}'


class Modules(models.Model, HitCountMixin):
    '''Modules creation'''

    class Meta:
        verbose_name = 'Module'
        verbose_name_plural = 'Modules'

    course = models.ForeignKey(Courses, on_delete=models.CASCADE, null=True, blank=True)

    title = models.CharField(max_length=256,unique=True)
    search = models.CharField(default='',editable=False,max_length=512)
    slug = models.SlugField(editable=False,max_length=256)
    subtitle = models.CharField(max_length=256, blank=True)

    module = RichTextUploadingField(external_plugin_resources=[('exportpdf','/static/articles/js/exportpdf/','plugin.js')], default='')
    tags = TaggableManager(blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    publish_date = models.DateTimeField()


    def save(self, *args, **kwargs):
        self.slug = slugify(unidecode(self.title))
        self.search = ''.join(c for c in unicodedata.normalize('NFD', self.title.lower() + ' ' + self.subtitle.lower() ) if unicodedata.category(c) != 'Mn')
        super().save(*args, **kwargs)



    def get_admin_url(self):
        content_type = ContentType.objects.get_for_model(self.__class__)
        return reverse("admin:%s_%s_change" % (content_type.app_label, content_type.model), args=(self.id,))

    def __str__(self):
        return f'{self.title}'