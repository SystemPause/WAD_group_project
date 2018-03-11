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


class ContactAdmin(admin.ModelAdmin):
    list_display = ("contacter","contactee","score")
    def contacter(self,obj):
        return obj.sourceUser.user.username
    def contactee(self,obj):
        return obj.contactedUser.user.username



# Models Registration.

admin.site.register(Language)
admin.site.register(Contact,ContactAdmin)
admin.site.register(UserProfile,ProfileAdmin)