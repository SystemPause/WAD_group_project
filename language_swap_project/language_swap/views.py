# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import pycountry
from django.shortcuts import render
from language_swap.models import UserProfile, Language, Contact
from language_swap.helperFunctions import getUserDetails
from django.contrib.auth.decorators import login_required

def index(request):
    context_dict = {'languages': []}

    # Get all languages from the database
    languages = Language.objects.all().order_by('LanguageName')

    # Populate the context_dictionary with all the languages
    for language in languages:
        context_dict['languages'].append(str(language).lower())

    return render(request, 'language_swap/index.html', context_dict)


def searchResult(request):
    context_dict = {'errors':[], 'users' : {}}
    errors = False

    # Get the parameters passed in the URL
    practicingLanguage = request.GET.get('practicingLanguage', '').encode('utf-8').lower().strip()
    spokenLanguage = request.GET.get('spokenLanguage', '').encode('utf-8').lower().strip()

    # Get a list of places. The list has the format ['city','province','country']
    places = request.GET.get('places', '').split(",")

    # Remove all the empty Unicode values from the list
    places = [place for place in places if place != u'']

    # If the list of places is not empty, process the values, otherwise add an error element
    # to the errors list
    if places:
        city = places[0].encode('utf-8').lower().strip()
        country = places[-1].encode('utf-8').lower().strip()
    else:
        errors = True
        context_dict['errors'].append("An error has occured while fetching the places.")

    # Try to retrieve the selected languages
    try:
        practicing = Language.objects.get(LanguageName = practicingLanguage)
        spoken = Language.objects.get(LanguageName = spokenLanguage)
    except:
        errors = True
        context_dict['errors'].append("An error has occured while fetching the languages.")

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

@login_required
def profile(request):
    context_dict = {'userProfile' : {}}

    loggedUser = UserProfile.objects.get(user = request.user)

    # Get all the details of the current logged in user
    context_dict['userProfile'].update(getUserDetails(loggedUser))

    return render(request, 'language_swap/profile.html', context_dict)

@login_required
def contactHistory(request):
    context_dict = {'contacts' : {}}

    # Get the current UserProfile object
    loggedUser = UserProfile.objects.get(user = request.user)

    # Get the contact list of the users that have been contacted by the logged in user
    contactList = Contact.objects.filter(sourceUser = loggedUser)

    for contact in contactList:
        # Populate the context_dict with contacts details
        context_dict['contacts'].update(getUserDetails(contact.contactedUser))

    return render(request, 'language_swap/contactHistory.html', context_dict)
