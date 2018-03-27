# Helper functions

# Import packages
from datetime import date
from language_swap.models import Contact
import requests
from django.core.mail import send_mail
from django.conf import settings

# This function retrieves all the informatin regarding one single User.
# It receives a user (UserProfile) object as parameter and
# it returns a dictionary that maps a unique username to a dictionary that
# contains all the details of the specified user.

def getUserDetails(userObject):
    user_dictionary = {}

    # Map a username to all the user's details
    user_dictionary[userObject.user.username] = {
        'id': userObject.user.id,
        'email' : userObject.user.email,
        'firstname' : userObject.user.first_name,
        'lastname' : userObject.user.last_name,
        'age' : getUserAge(userObject.dob),
        'country' : userObject.country,
        'city' : userObject.city,
        'picture' : userObject.picture if bool(userObject.picture) else False,
        'hobby' : userObject.hobby if bool(userObject.hobby) else False,
        'speaks' : userObject.speaks.all(),
        'practices' : userObject.practices.all(),
        'gender' : userObject.gender,
        'score' : getUserRating(userObject)
    }

    return user_dictionary

# The function computes the age of a specified user. It gets the user date of birth as
# parameter and returns the age

def getUserAge(dateOfBirth):
    todayDate = date.today()
    yearsDifference = todayDate.year - dateOfBirth.year

    # Check if the birthday month and day have already passed or not
    monthDayCheck = ((todayDate.month, todayDate.day) < (dateOfBirth.month, dateOfBirth.day))

    return  yearsDifference - monthDayCheck

# The function getUserRating(currentobject) computes the rating of a given user.
# It returns False if the user has not been rated yet

def getUserRating(currentUser):

    # Get the UserProfile object corresponding to the specified user
    contactsObject = Contact.objects.filter(contactedUser = currentUser)

    if contactsObject.exists():
        # The variable finalScore is used in order to keep track of the user score.
        finalScore = 0.0
        # Counter is used in order to keep track how many users have rated another user
        counter = 0

        # Compute the score only for users where the score is not 0 (default value: user not rated yet)
        for contactObject in contactsObject:
            if(contactObject.score != 0):
                finalScore +=  contactObject.score
                counter += 1

        # If the variable counter is 0 then it means that someone has already contacted the current users
        # but nobody has rated it. So return False. Otherwise return the user rating
        if counter == 0:
            return False
        else:
            return round(finalScore / counter,1)
    else:
        return False

# The function calls the google maps Api in order to retrieve the city and the country of a specific location.
# It returns a dictionary that countains 3 different key.
# - status: True if the operation has been completed successfully, False otherwise
# - city: the city of the specified location
# - country: the country of the specified location

def placesReverseGeocoder(location):

    resultDict = {'status' : False, 'city' : '', 'country' : ''}
    geocode_url = "https://maps.googleapis.com/maps/api/geocode/json?address=" + location + "&key=AIzaSyD0WYZr005e3brFlluhm2dUStd1bmZ5jec&language=en"

    # Try to get and retireve the json object from the specified URL
    try:
        results = requests.get(geocode_url)
        results = results.json()
    except:
        return resultDict
    # If status is 'OK' then no errors occurred; the address was successfully parsed and
    # at least one geocode was returned
    if results['status'] == 'OK':
        # Try to fetch the Json object to retrieve the city and the country
        try:
            for el in results['results'][0]['address_components']:
                if 'locality' in el['types']:
                    resultDict['city'] = el['long_name'].lower()
                if 'country' in el['types']:
                    resultDict['country'] = el['long_name'].lower()
        except:
            return resultDict

    # Check if the city and the country have a value
    if resultDict['city'] and resultDict['country']:
        resultDict['status'] = True
        return resultDict
    else:
        return resultDict


# The function sends an email to one user from one user. If something fails return False,
# otherwise return true

def sendEmailFunction(loggedUser, emailTo, message):
    hostEmail = settings.EMAIL_HOST_USER
    loggedUserEmail = loggedUser.user.email
    loggedUserName = loggedUser.user.first_name + " " + loggedUser.user.last_name
    defaultMessage = "You have a new message from " + loggedUserName + ". \n\n\t" + message + "\n\n Contact " + loggedUserName + " at " + loggedUserEmail
    object = "Language Swap: You have a new message from " + loggedUserName + "!"
    try:
        send_mail(object, defaultMessage, hostEmail, [emailTo], fail_silently = True)
    except:
        return False
    return True
