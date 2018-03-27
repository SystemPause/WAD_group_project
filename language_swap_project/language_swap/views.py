# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from language_swap.models import User, UserProfile, Language, Contact
from language_swap.forms import EditProfileForm, DeleteAccountForm
from language_swap.helperFunctions import getUserDetails, getUserRating, placesReverseGeocoder, sendEmailFunction
from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.urls import reverse
import json


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

    # get the place from the Get request and pass it as a parameter to the placesReverseGeocoder function
    places = placesReverseGeocoder(request.GET.get('places', ''))

    # If the function returns True, retrieve the city and the country Otherwise generate an error
    if places['status']:
        city = places['city']
        country = places['country']
    else:
        errors = True
        context_dict['errors'].append("An error has occurred while fetching the places.")


    # Try to retrieve the selected languages
    try:
        practicing = Language.objects.get(LanguageName = practicingLanguage)
        spoken = Language.objects.get(LanguageName = spokenLanguage)
    except Language.DoesNotExist:
        errors = True
        context_dict['errors'].append("An error has occurred while fetching the languages.")

    # If an error occurs while selecting the languages, do not perform the Query and
    # just return the error message
    if not errors:
        resultUsers = UserProfile.objects.filter(practices= spoken, speaks = practicing, country = country, city = city)

        # If there are results to the Query, retrieve users details
        if resultUsers.exists():
            for resultUser in resultUsers:
                # Check if the user is logged in. We don't want to show the logged in user in the result page
                if request.user.is_authenticated():
                    # If it is not logged in, add it to the result context dictionary
                    if request.user != resultUser.user:
                        context_dict['users'].update(getUserDetails(resultUser))
                else:
                    context_dict['users'].update(getUserDetails(resultUser))
        else:
            context_dict['errors'].append("There are no matches in this city.")

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
def edit_profile(request):
    loggedUser = UserProfile.objects.get(user=request.user)

    form = EditProfileForm(request.POST or None, initial={'places': loggedUser.city.title()+","+loggedUser.country.title(),
                                                          'hobby': loggedUser.hobby, 'picture': loggedUser.picture})
    if request.method == 'POST':
        if form.is_valid():
            loggedUser.city = form.cleaned_data['city']
            loggedUser.country = form.cleaned_data['country']
            loggedUser.hobby = form.cleaned_data['hobby']
            if 'picture' in request.FILES:
                loggedUser.picture.delete(save=False)
                loggedUser.picture = request.FILES['picture']
            loggedUser.save()
            return HttpResponseRedirect(reverse('myProfile'))

    context = {'form': form, 'userProfile': {}}
    # Gets all the details of the current logged in user
    context['userProfile'].update(getUserDetails(loggedUser))

    return render(request, 'language_swap/edit_profile.html', context)

@login_required
def delete_account(request):
    form = DeleteAccountForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            user = request.user
            loggedUser = UserProfile.objects.get(user=user)
            loggedUser.picture.delete(save=False)
            loggedUser.delete()
            user.delete()
            return HttpResponseRedirect(reverse(index))

    context = {'form': form}
    return render(request, 'language_swap/delete_account.html', context)

@login_required
def contactHistory(request):
    context_dict = {'contacts' : {}}

    # Get the current UserProfile object
    loggedUser = UserProfile.objects.get(user = request.user)

    # Get the contact list of the users that have been contacted by the logged in user
    contactList = Contact.objects.filter(sourceUser = loggedUser)

    for contact in contactList:

        # Temporary dictionary containing all contact details
        tempDict = getUserDetails(contact.contactedUser)
        # Update the dictionary with the score assigned by the current logged in user to the specific contact
        tempDict[contact.contactedUser.user.username]['assignedScore'] = contact.score
        # Populate the context_dict with contacts details
        context_dict['contacts'].update(tempDict)

    return render(request, 'language_swap/contactHistory.html', context_dict)

# This view is used in order to perform the Ajax request to update an user rating.
# If one of the necessary steps fails, return False
@login_required
def rating(request):

    # Check if the request made is Ajax. In this way we prevent users from accessing directly to the
    # url under the name 'rating'. If the request is not Ajax, raise a Http404 error
    if request.is_ajax():

        # The resultDict is used in order to keep track of the rating process. if it fails, the
        # result value is set to False. The score key is used to store the new score for the current user
        resultDict = {'result' : False, 'score' : ''}

        loggedUser = UserProfile.objects.get(user = request.user)

        # Get the values attached to the GET request
        ratedUserId = request.GET.get('ratedUserId' , '').strip().lower()
        rating = request.GET.get('rating' , '').strip().lower()

        # Check if the values are empty or not. If they are empty, return false
        if ratedUserId and rating:
            # Try to get the ratedUser object and check if the loggedIn user has concacted it.
            # If not, return False
            try:
                rating = int(rating)
                ratedUser = User.objects.get(id = ratedUserId)
                ratedUser = UserProfile.objects.get(user = ratedUser)
                contactObject = Contact.objects.get(sourceUser = loggedUser, contactedUser = ratedUser)
            except:
                return HttpResponse(json.dumps(resultDict))
            # The rating system accepts values from 1 to 5. Therefore, check if the rating value
            # can be accepted and then set the rating of the ratedUser to be equal to rating
            # (the one specified by the loggedIn user).
            if rating in range(1,6):
                contactObject.score = rating
                contactObject.save()
                resultDict['score'] = getUserRating(ratedUser)
                resultDict['result'] = True
                return HttpResponse(json.dumps(resultDict))
            else:
                return HttpResponse(json.dumps(resultDict))
        else:
            return HttpResponse(json.dumps(resultDict))
    else:
        raise Http404

# The function checks if a given email is inside the db. If the email is contained, return 1
# otherwise return 0
def emailCheck(request):
    if request.is_ajax():
        emailList = User.objects.all().values_list('username',flat = True)
        email = request.GET.get('email','').strip().lower()

        if email in emailList:
            return HttpResponse(1)
        else:
            return HttpResponse(0)
    else:
        raise Http404


# The sendEmail function is used in order to send a mail to a User. It returns True if
# the email has been sent successfully, False otherwise.
@login_required
def sendEmail(request):
    # Check if the request performed is Ajax, if it's not raise a 404 error
    if request.is_ajax():

        # Get the contact User id and the message
        sendMessageToUser = request.GET.get('userId','').strip()
        message = request.GET.get('message','').strip()
        if sendMessageToUser and message:
            # Get the current logged In user
            loggedUser = UserProfile.objects.get(user = request.user)
            try:
                sendMessageToUser = int(sendMessageToUser)
                # Try to retrieve the user with the specified id
                contactUser = User.objects.get(id = sendMessageToUser)
                contactUser = UserProfile.objects.get(user = contactUser)
            except:
                return HttpResponse(False)
            # Send the email to the specified user, if something fails return False
            if sendEmailFunction(loggedUser, contactUser.user.email, message):
                # If the email has been sent successfully, try to create a new Contact
                try:
                    contactCreated = Contact.objects.get_or_create(sourceUser = loggedUser, contactedUser = contactUser)
                except:
                    return HttpResponse(False)
                return HttpResponse(True)
        return HttpResponse(False)
    else:
        raise Http404
