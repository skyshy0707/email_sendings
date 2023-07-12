# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin

from . import models

# Register your models here.
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('username', 'email')

admin.site.register(models.Subscriber, SubscriberAdmin)