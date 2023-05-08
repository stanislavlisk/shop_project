from django.contrib.auth.models import User, Group  # siuntėjas
from django.db.models.signals import post_save  # signalas
from django.dispatch import receiver  # gavėjo dekoratorius

from .models import UserProfile, Cart


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
        instance.groups.add(Group.objects.get(name='shop_users'))
    else:
        instance.userprofile.save()
    print(instance, created)


@receiver(post_save, sender=User)
def add_cart(sender, instance, created, **kwargs):
    if created:
        Cart.objects.create(user=instance)
    # else:
    #     instance.cart.save()
    print(instance, created)