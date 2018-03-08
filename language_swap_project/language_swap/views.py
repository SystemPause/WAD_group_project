# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render

# LanguageSwap Specific 
from django.http import HttpResponse
from django.shortcuts import render
from language_swap.models import UserProfile, Language, Contact
 
import pycountry


def index(request):
    context_dict = {}
    
    # Get all languages from the database
    languages = Language.objects.all()
    
    # Populate a temporary list with all the languages
    languages_list = []
    for language in languages:
        languages_list.append(str(language).lower())
        
    # Populate a temporary list with all the countries
    country_list = []
    for country in pycountry.countries:
        print(country.name)
        country_list.append(country.name.lower())
    
    # Sort the elements of the list alphabetically
    languages_list.sort()
    country_list.sort()
    
    # Populate the context dictionary
    context_dict['languages'] = languages_list
    context_dict['countries'] = country_list
        
    return render(request, 'language_swap/index.html', context_dict)
    
    
def searchResult(request):
    context_dict = {}
    # Change the file name for a more appropriate one
    return render(request, 'language_swap/result.html', context_dict)

def about(request):
    context_dict = {}
    
    return render(request, 'language_swap/about.html', context_dict)

def team(request):
    context_dict = {}
    
    return render(request, 'language_swap/team.html', context_dict)

def contact(request):
    context_dict = {}
    
    return render(request, 'language_swap/contact.html', context_dict)