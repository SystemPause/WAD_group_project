# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import pycountry
from django.shortcuts import render

from language_swap.helperFunctions import getUserDetails
from language_swap.models import UserProfile, Language


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
        country_list.append(country.name.lower())
    
    # Sort the elements of the list alphabetically
    languages_list.sort()
    country_list.sort()
    
    # Populate the context dictionary
    context_dict['languages'] = languages_list
    context_dict['countries'] = country_list
        
    return render(request, 'language_swap/index.html', context_dict)
    
    
def searchResult(request):
    context_dict = {'errors':[], 'users' : {}}
    errors = False
    
    # Get the parameters passed in the URL
    practicingLanguage = request.GET.get('practicingLanguage', '').encode('utf-8').lower().strip()
    spokenLanguage = request.GET.get('spokenLanguage', '').encode('utf-8').lower().strip()
    country = request.GET.get('country', '').encode('utf-8').lower().strip()
    city = request.GET.get('city', '').encode('utf-8').lower().strip()
    
    # Try to retrieve the selected languages
    try:
        practicing = Language.objects.get(LanguageName = practicingLanguage)
        spoken = Language.objects.get(LanguageName = spokenLanguage)
    except:
        errors = True
        context_dict['errors'].append("An error has occured while fetching the languages")
    
    # If an error occurs while selecting the languages, do not perform the Query and 
    # just return the error message
    if not errors:
        resultUsers = UserProfile.objects.filter(practices= spoken, speaks = practicing, country = country, city = city)
        
        # If there are results to the Query, retrieve users details
        if resultUsers.exists():
            for resultUser in resultUsers:
                context_dict['users'].update(getUserDetails(resultUser))      
        else:
            context_dict['errors'].append("There are no users in this city.")
            
            
    # TODO Change the file name for a more appropriate one
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

