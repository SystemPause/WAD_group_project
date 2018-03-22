# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
# Create your models here.

class Language(models.Model):
    
    LanguageName = models.CharField(max_length=120,primary_key=True)

    def __str__(self):
        return self.LanguageName


class UserProfile(models.Model):

    #these are the user details that are not in the default User model
    user = models.OneToOneField(User)

    city = models.CharField(max_length=120)

    country = models.CharField(max_length=120)

    gender = models.CharField(max_length=10,  null = True)

    #picture and hobby are optional
    picture = models.ImageField(upload_to='profile_images',blank = True)

    hobby = models.CharField(max_length=500,blank = True)

    # following lines are to calculate age from date of birth
    #age can be calculated in views.py
    dob = models.DateField(max_length=8, null = True)

    #these are the relationship attributes between user and languages
    speaks = models.ManyToManyField(Language,related_name="speaks")

    practices = models.ManyToManyField(Language,related_name='practices')

    def __str__(self):
        return self.user.username


class Contact(models.Model):
    sourceUser = models.ForeignKey(UserProfile,related_name='source')
    contactedUser = models.ForeignKey(UserProfile,related_name='contacted')

    #by default, if a user appears on your contact history, he/she is not rated by default
    score = models.IntegerField(default=0)







