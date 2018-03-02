# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User


from django.db import models
# Create your models here.

class Language(models.Model):

    LanguageName = models.CharField()

    def __str__(self):
        return self.LanguageName


class UserProfile(models.Model):

    #these are the user details that are not in the default User model
    user = models.OneToOneField(User)

    city = models.CharField()

    country = models.CharField()

    picture = models.ImageField(upload_to='profile_images',blank = True)

    hobby = models.CharField(max_length=500,blank = True)

    rating = models.ManyToManyField('self',through=Rate,symmetrical=False)

    #these are the relationship attributes between user and languages
    speaks = models.ManyToManyField(Language)

    practices = models.ManyToManyField(Language)

    #these are the relationship attributes between different users
    contacts = models.ManyToManyField('self')

class Rate(models.Model):
    ratedUser = models.ForeignKey(UserProfile)

    rater = models.ForeignKey(UserProfile)

    scoreChoices = (
        (1, "bad"),
        (2, "not too bad"),
        (3, "normal"),
        (4, "kinda good"),
        (5, "good"),
    )

    score = models.IntegerField(choices = scoreChoices)


    def __str__(self):
        return self.user.username