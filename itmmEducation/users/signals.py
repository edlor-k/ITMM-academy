from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile, Token

@receiver(post_save, sender=User)
def create_user_related_objects(sender, instance, created, **kwargs):
    """
    Создаёт объект Profile и Token при создании нового пользователя.
    """
    if created:
        Profile.objects.create(user=instance)
        Token.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_related_objects(sender, instance, **kwargs):
    """
    Сохраняет связанные объекты Profile и Token при сохранении пользователя.
    """
    if hasattr(instance, 'profile'):
        instance.profile.save()
    if hasattr(instance, 'token'):
        instance.token.save()