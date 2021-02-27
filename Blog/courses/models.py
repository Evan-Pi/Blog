from django.db import models
from taggit.managers import TaggableManager
from django.utils.text import slugify
from unidecode import unidecode
import unicodedata
from django_currentuser.middleware import (get_current_user, get_current_authenticated_user)
from django.urls import reverse
from django.contrib.contenttypes.models import ContentType
from django.utils.html import mark_safe
from django.core.validators import MinValueValidator
from hitcount.models import HitCount, HitCountMixin
from django.contrib.contenttypes.fields import GenericRelation
from froala_editor.fields import FroalaField

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
    title = models.CharField(max_length=150,unique=True)
    search = models.CharField(default='',editable=False,max_length=472)
    slug = models.SlugField(editable=False,max_length=150)
    description = models.TextField(max_length=256, blank=True)
    image = models.ImageField(upload_to = "Courses_Images", default='')
    use_image_as_background_in_course = models.BooleanField(default=True)

    tags = TaggableManager(blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    publish_date = models.DateTimeField()

    hit_count_generic = GenericRelation(HitCount, object_id_field='object_pk',related_query_name='hit_count_generic_relation')


    author = models.CharField(editable=False, default='', max_length=64)

    approved = models.BooleanField(default=False)

    def image_tag(self):
        return mark_safe(f'<img src="{self.image.url}" width="auto" height="55" />')

    image_tag.short_description = 'Image preview'

    def save(self, *args, **kwargs):
        self.slug = slugify(unidecode(self.title))
        if not self.id:
            self.author = get_current_user().email

        if self.description:
            self.search = ''.join(c for c in unicodedata.normalize('NFD', self.title.lower() + ' ' + self.description.lower() + ' ' + self.author.lower() ) if unicodedata.category(c) != 'Mn')
        else:
            self.search = ''.join(c for c in unicodedata.normalize('NFD', self.title.lower() + ' ' + self.author.lower() ) if unicodedata.category(c) != 'Mn')
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('course', args=[self.slug])

    def get_admin_url(self):
        content_type = ContentType.objects.get_for_model(self.__class__)
        return reverse("admin:%s_%s_change" % (content_type.app_label, content_type.model), args=(self.id,))

    def __str__(self):
        return f'{self.title}'



class Modules(models.Model, HitCountMixin):
    '''Modules creation'''

    class Meta:
        verbose_name = 'Module'
        verbose_name_plural = 'Modules'

    course = models.ForeignKey(Courses, on_delete=models.CASCADE, null=True, blank=True)

    title = models.CharField(max_length=150,unique=True)
    search = models.CharField(default='',editable=False,max_length=300)
    slug = models.SlugField(editable=False,max_length=150)
    subtitle = models.CharField(max_length=150, blank=True)

    module = FroalaField()
    tags = TaggableManager(blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    publish_date = models.DateTimeField()

    order = models.IntegerField(validators=[MinValueValidator(1)], blank=True, default=1)



    def save(self, *args, **kwargs):
        self.slug = slugify(unidecode(self.title))
        self.search = ''.join(c for c in unicodedata.normalize('NFD', self.title.lower() + ' ' + self.subtitle.lower() ) if unicodedata.category(c) != 'Mn')
        super().save(*args, **kwargs)



    def get_admin_url(self):
        content_type = ContentType.objects.get_for_model(self.__class__)
        return reverse("admin:%s_%s_change" % (content_type.app_label, content_type.model), args=(self.id,))

    def __str__(self):
        return f'{self.title}'