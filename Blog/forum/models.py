from django.db import models
from django_currentuser.middleware import (get_current_user, get_current_authenticated_user)
from taggit.managers import TaggableManager
from django.utils.text import slugify
from unidecode import unidecode
import unicodedata
from hitcount.models import HitCount, HitCountMixin
from django.contrib.contenttypes.fields import GenericRelation

class Discussions(models.Model, HitCountMixin):
    class Meta:
        verbose_name = 'Discussions'
        verbose_name_plural = 'Discussion'

    title = models.CharField(max_length=250,unique=True)
    created = models.DateTimeField(auto_now_add=True)
    discussion = models.TextField()
    tags = TaggableManager(blank=True)
    search = models.CharField(default='',editable=False,max_length=472)
    slug = models.SlugField(editable=False,max_length=150)
    author = models.CharField(editable=False, default='', max_length=64)
    approved = models.BooleanField(default=True)

    hit_count_generic = GenericRelation(HitCount, object_id_field='object_pk',related_query_name='hit_count_generic_relation')


    def save(self, *args, **kwargs):
        self.slug = slugify(unidecode(self.title))
        if not self.id:
            self.author = get_current_user().username
        self.search = ''.join(c for c in unicodedata.normalize('NFD', self.title.lower()  + ' ' + self.author.lower() ) if unicodedata.category(c) != 'Mn')
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('forum', args=[self.slug, self.pk])


    def __str__(self):
        return self.title