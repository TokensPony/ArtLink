from __future__ import unicode_literals

from django.db import models
from django.core.validators import *

from django.contrib.auth.models import User, Group

from django.db.models.signals import post_save
from django.dispatch import receiver

from django.contrib import admin
import base64


'''
The model for profile information about the artist that is linked one-to-one with the
corresponding user data in the default user model and an implicit one to many relationship
with the commission data created by the user.
'''
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name = 'profile')
    commstatus = models.CharField(max_length=1000, blank=False, default = '')
    description = models.TextField(max_length=1000, blank=False, default = '')
    artstyle = models.CharField(max_length=1000, blank=False, default = '')
    willdraw = models.CharField(max_length=1000, blank=False, default = '')
    wontdraw = models.CharField(max_length=1000, blank=False, default = '')
    img = models.CharField(max_length=1000, blank=False, default = 'img/no-image.jpg')

    #commissions = implicit one to many relatonship with the commissions created by the user
    def __str__(self):
        return str(self.user)

    class JSONAPIMeta:
        resource_name = "profiles"


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user',)

'''
Information about a particular piece of commission info including description, slots, price,
and the profile that the commission belongs to
'''
class Commission(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE,  related_name = 'commissions')
    commtype = models.CharField(max_length=1000, blank=True)
    description = models.TextField(max_length=1000, blank=True)
    price_min = models.DecimalField(max_digits=5, decimal_places=2, blank=True)
    price_max = models.DecimalField(max_digits=5, decimal_places=2, blank=True)
    slots = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(99)], blank=True)

    def __str__(self):
        return str(self.profile) + str(self.commtype)

    class JSONAPIMeta:
        resource_name = "commissions"

class CommissionAdmin(admin.ModelAdmin):
    list_display = ('profile', 'commtype')
