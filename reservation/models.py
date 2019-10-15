from django.db import models

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import uuid


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.TextField(max_length=500, blank=True)
    last_name = models.TextField(max_length=500, blank=True)
    birth_date = models.DateField(null=True, blank=True)

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()


class Parking_space(models.Model):
    parking_number = models.UUIDField(default=uuid.uuid4)

class Reservation(models.Model):
    start_date = models.DateField()
    finish_date = models.DateField()
    parking_space_number = models.ForeignKey(Parking_space, null=True,
                                             related_name="parking_space", on_delete=models.SET_NULL)
    phone_number = models.CharField(max_length=16)
    profile = models.ForeignKey(Profile, null=True,
                                             related_name="reservation", on_delete=models.SET_NULL)
    

   
