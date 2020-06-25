from django.contrib.auth.models import AbstractUser
from django.db import models
from PIL import Image

from django.db.models.signals import post_save 
from django.dispatch import receiver

from articles.models import Articles

class Account(AbstractUser):

    class Meta:
        verbose_name = 'Account'
        verbose_name_plural = 'Accounts'
        
    email = models.EmailField(unique=True)

    REQUIRED_FIELDS = ['username']
    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.username


class Profile(models.Model):
    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

    def viewed_articles_list(self):
        return [article.title for article in self.viewed_articles.all()]

    user = models.OneToOneField(Account, on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to = "Users_Profile_Images", blank=True, default='')

    viewed_articles = models.ManyToManyField(Articles, through='ArticlesViews')

    def __str__(self):
        return f'{self.user.username}'

    def save(self,*args, **kwargs):
        super(Profile, self).save(*args, **kwargs)
        
        if self.profile_image:
            img = Image.open(self.profile_image.path)
            if img.height > 450 or img.width > 450:
                output_size = (450,450)
                img.thumbnail(output_size)
                img.save(self.profile_image.path)
        else:
            pass



class ArticlesViews(models.Model):
    class Meta:
        verbose_name = 'User History - Article view'
        verbose_name_plural = 'User History - Articles views'

    article = models.ForeignKey(Articles, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

@receiver(post_save, sender=Account)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)