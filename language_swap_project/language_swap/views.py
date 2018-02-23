# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render

# Mine
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse


def index(request):
    context_dict = {'message': 'This is the index page.'}
    return render(request, 'language_swap/index.html', context_dict)
