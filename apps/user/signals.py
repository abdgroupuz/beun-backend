from django.db.models import signals
from django.dispatch import receiver

from .models import User
from apps.market.models import Cart


@receiver(signal=signals.post_save, sender=User)
def post_save_user(sender, instance, created, *args, **kwargs):
    if created:
        cart, __ = Cart.objects.get_or_create(user=instance)
        cart.save()
