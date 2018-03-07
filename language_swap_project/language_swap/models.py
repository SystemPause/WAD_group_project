# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User


from django.db import models
# Create your models here.

class Language(models.Model):

    LanguageName = models.CharField(max_length=120)

    def __str__(self):
        return self.LanguageName


class UserProfile(models.Model):

    #these are the user details that are not in the default User model
    user = models.OneToOneField(User)

    city = models.CharField(max_length=120)

    country = models.CharField(max_length=120)

    picture = models.ImageField(upload_to='profile_images',blank = True)

    hobby = models.CharField(max_length=500,blank = True)

    #these are the relationship attributes between user and languages
    speaks = models.ManyToManyField(Language,related_name="speak")

    practices = models.ManyToManyField(Language,related_name='practice')

    #these are the relationship attributes between different users
    #contacts = models.ManyToManyField('self',related_name='contact',
                                      #symmetrical=False)

    def __str__(self):
        return self.user.username


class Contact(models.Model):
    sourceUser = models.ForeignKey(UserProfile,related_name='source')
    contactedUser = models.ForeignKey(UserProfile,related_name='contacted')
    scoreChoices = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
    )

    score = models.IntegerField(choices=scoreChoices)













