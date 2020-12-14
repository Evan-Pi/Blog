from django.contrib.auth.models import *
from django.db import models
from django.utils.html import mark_safe
from . managers import AccountManager
from unidecode import unidecode
import unicodedata

from articles.models import Articles
from courses.models import Courses

class Account(AbstractUser):
    class Meta:
        verbose_name = 'Account'
        verbose_name_plural = 'Accounts'

    username = None
    email = models.EmailField(unique=True, blank=False)
    profile_image = models.ImageField(upload_to = "Users_Profile_Images", blank=True, default='', verbose_name = "Profile Photo")

    first_name_slug = models.CharField(max_length=150, editable=False, default='',blank=True)
    last_name_slug = models.CharField(max_length=150, editable=False, default='',blank=True)
    full_name_slug = models.CharField(max_length=300, editable=False, default='',blank=True)

    objects = AccountManager()

    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'email'

    def __str__(self):
        if self.first_name or self.last_name:
            username = f"{self.first_name} {self.last_name} - {self.email}"
        else:
            username = f"{self.email}"
        return username

    def Slug(string_to_slugify):
        slug = ''.join(c for c in unicodedata.normalize('NFD', string_to_slugify.lower() ) if unicodedata.category(c) != 'Mn').strip()
        return slug

    def image(self):
        if self.profile_image:
            p_img = mark_safe(f'<div style="width:80px; height:50px;  background-image:url({self.profile_image.url}); background-position: center; background-size: contain; background-repeat: no-repeat;"></div>')
        else:
            p_img = mark_safe(f'<div style="width:80px; height:50px; display:flex; flex-direction:column; justify-content:center; aligh-items:center;"><small style="font-size:9px;">NO IMAGE AVAILABLE</small></div>')
        return p_img
    image.short_description = 'Preview'

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def save(self,*args, **kwargs):
        self.first_name_slug = Account.Slug(self.first_name)
        self.last_name_slug = Account.Slug(self.last_name)
        self.full_name_slug = Account.Slug(self.first_name + self.last_name)
        super(Account, self).save(*args, **kwargs)



class Profile(models.Model):
    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'
        

    def viewed_articles_list(self):
        return [article.title for article in self.viewed_articles.all()]

    user = models.ForeignKey(Account, on_delete=models.CASCADE)

    viewed_articles = models.ManyToManyField(Articles, through='ArticlesViews')
    viewed_courses = models.ManyToManyField(Courses, through='CoursesViews')

    def __str__(self):
        return f'{self.user.email}'


class ArticlesViews(models.Model):
    class Meta:
        verbose_name = 'Article view'
        verbose_name_plural = 'Articles views'

    article = models.ForeignKey(Articles, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

class CoursesViews(models.Model):
    class Meta:
        verbose_name = 'Course view'
        verbose_name_plural = 'Courses views'

    course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)



