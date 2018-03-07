# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from language_swap.models import Language,UserProfile,Contact

admin.site.register(Language)
admin.site.register(Contact)
admin.site.register(UserProfile)

from django.contrib import admin

# Register your models here.
