import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'language_swap_project.settings')

import django
django.setup()
from language_swap.models import UserProfile,Language,Contact,User
import pycountry

def populate():
    language_list = []
    for language in pycountry.languages:
        language_list.append(language.name.lower())
        add_Language(language.name.lower())



    user_list = [
        {
            "firstname": "Dicky", "lastname":"Donkey","username":"lamborghini", "email": "dickd@dd.com",
            "password":"hunter123","city":"Milan","country":"Italy",
            "speaks":["italian","french"],"practices":["burmese","english"]
        },

        {
            "firstname": "Nay Min", "lastname": "Htet","username":"joker111", "email": "naymin@htet.com",
            "password": "hunter123", "city": "Mandalay", "country": "Myanmar",
            "speaks":["burmese","spanish"],"practices":["italian","english"]
        },

    ]
    print(UserProfile._meta.get_fields())
    for user in user_list:
        speaksList = []

        for sth in user["speaks"]:
            speaksList.append(Language.objects.get(LanguageName = sth))


        practicesList = []

        for sth in user["practices"]:
            practicesList.append(Language.objects.get(LanguageName=sth))


        add_user(user["firstname"],user["lastname"],user["username"],user["email"],user["password"],user["city"],user["country"],speaksList,practicesList)





def add_Language(name):
    l = Language.objects.get_or_create(LanguageName = name)[0]
    l.save()
    return l

def add_user(firstname,lastname,username,email,password,city,country,speaks,practices):

    userObject = User.objects.get_or_create(first_name = firstname, last_name = lastname,username =username,  email = email,
                                    password = password)[0]
    userObject.set_password(userObject.password)
    userObject.save()



    userProfile = UserProfile.objects.get_or_create(user = userObject, city = city,
                                             country = country)[0]
    print(userObject)
    print(userProfile)
    userProfile.save()

    for sth in speaks:
        userProfile.speaks.add(sth)

    for sth in practices:
        userProfile.practices.add(sth)

    return userObject,userObject
#



if __name__ == '__main__':
    print("Starting Rango population script")
    populate()