# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from django.db import models

from language_swap.models import Language,UserProfile,Contact


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','city','country',)
    def first_name(self,obj):
        return obj.user.first_name
    def last_name(self,obj):
        return obj.user.last_name

admin.site.register(Language)
admin.site.register(Contact)
admin.site.register(UserProfile,ProfileAdmin)

from django.contrib import admin

# Register your models here.
