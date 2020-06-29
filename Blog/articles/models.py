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

class ArticlesCategories(models.Model):
    '''Articles categories creation'''

    class Meta:
        verbose_name = 'Article Category'
        verbose_name_plural = 'Articles Categories'

    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(editable=False,max_length=100,default='')
    image = models.ImageField(upload_to = "Articles_Categories_Images", default='', blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(unidecode(self.title))
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class Articles(models.Model, HitCountMixin):
    '''Articles creation'''

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'

    category = models.ForeignKey(ArticlesCategories, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.TextField(max_length=256,unique=True)
    search = models.CharField(default='',editable=False,max_length=512)
    slug = models.SlugField(editable=False,max_length=256)
    subtitle = models.TextField(max_length=256, blank=True)
    image = models.ImageField(upload_to = "Articles_Images", default='')
    use_image_as_background_in_article = models.BooleanField(default=True)

    article = RichTextUploadingField(external_plugin_resources=[('exportpdf','/static/articles/js/exportpdf/','plugin.js')])
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
        return reverse('article', args=[self.slug])

    def get_admin_url(self):
        content_type = ContentType.objects.get_for_model(self.__class__)
        return reverse("admin:%s_%s_change" % (content_type.app_label, content_type.model), args=(self.id,))

    def __str__(self):
        return self.title

class Comments(models.Model):
    '''This class creates comments for articles'''

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

    article = models.ForeignKey(Articles, on_delete=models.CASCADE)
    author = models.CharField(max_length=256)
    author_image = models.ImageField(upload_to = "Comments_Author_Images", default='',blank=True)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    approved_comment = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.author} | {self.text[:60]}" + "..."

class SubComments(models.Model):
    '''This class creates subcomments for comments'''

    class Meta:
        verbose_name = 'Subcomment'
        verbose_name_plural = 'Subcomments'

    comment = models.ForeignKey(Comments, on_delete=models.CASCADE)
    author = models.CharField(max_length=256)
    author_image = models.ImageField(upload_to = "Comments_Author_Images", default='',blank=True)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    approved_comment = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.author} | {self.text[:60]}" + "..."
