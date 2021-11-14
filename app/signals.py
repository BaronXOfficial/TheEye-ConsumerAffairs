from django.db.models.signals import post_save, pre_delete
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import UUIDEvent


@receiver(post_save, sender=User)
def create_event(sender, instance, created, **kwargs):
    if created:
        UUIDEvent.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_event(sender, instance, **kwargs):
    instance.event.save()