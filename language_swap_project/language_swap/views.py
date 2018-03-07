# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render

# Mine
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse
from language_swap.models import UserProfile


def index(request):
    context_dict = {'message': 'This is the index page.'}
    user_profile = UserProfile.objects.all()
    print(user_profile)
    return render(request, 'language_swap/index.html', context_dict)
    