from django.db.models.signals import post_save 
from django.dispatch import receiver
from . models import Account, Profile


@receiver(post_save, sender=Account)
def create_profile(sender, instance, **kwargs):
    profile, created = Profile.objects.get_or_create(user=instance)