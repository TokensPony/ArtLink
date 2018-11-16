from __future__ import unicode_literals

from django.db import models
from django.core.validators import *

from django.contrib.auth.models import User, Group

from django.db.models.signals import post_save
from django.dispatch import receiver

from django.contrib import admin
import base64

class Event(models.Model):
    eventtype = models.CharField(max_length=1000, blank=False)
    timestamp = models.DateTimeField()
    userid = models.CharField(max_length=1000, blank=True)
    requestor = models.GenericIPAddressField(blank=False)
    commstatus = models.CharField(max_length=1000, blank=False)
    description = models.CharField(max_length=1000, blank=False)
    name = models.CharField(max_length=1000, blank=False)

    def __str__(self):
        return str(self.eventtype)

class EventAdmin(admin.ModelAdmin):
    list_display = ('eventtype', 'timestamp')

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name = 'profile')
    commstatus = models.CharField(max_length=1000, blank=False, default = '')
    description = models.TextField(max_length=1000, blank=False, default = '')
    artstyle = models.CharField(max_length=1000, blank=False, default = '')
    willdraw = models.CharField(max_length=1000, blank=False, default = '')
    wontdraw = models.CharField(max_length=1000, blank=False, default = '')

    def __str__(self):
        return str(self.user)

    class JSONAPIMeta:
        resource_name = "profiles"

'''
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
'''

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user',)

class Commission(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    commtype = models.CharField(max_length=1000, blank=True)
    description = models.TextField(max_length=1000, blank=True)
    price_min = models.DecimalField(max_digits=5, decimal_places=2, blank=True)
    price_max = models.DecimalField(max_digits=5, decimal_places=2, blank=True)
    slots = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(99)], blank=True)

    def __str__(self):
        return str(self.user) + str(self.commtype)

class CommissionAdmin(admin.ModelAdmin):
    list_display = ('user', 'commtype')

class ApiKey(models.Model):
    owner = models.CharField(max_length=1000, blank=False)
    key = models.CharField(max_length=5000, blank=False)

    def __str__(self):
        return str(self.owner) + str(self.key)

class ApiKeyAdmin(admin.ModelAdmin):
    list_display = ('owner','key')
