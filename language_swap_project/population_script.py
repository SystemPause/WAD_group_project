import os
#from django.contrib.auth.models import User
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'language_swap_project.settings')

import django
django.setup()
from language_swap.models import UserProfile,Language,Contact

def populate():
    language_list = [
        "burmese", "italian", "english"
    ]

    for lang in language_list:
        add_Language(lang)


    '''
    user_list = [
        {
            "firstname": "Dicky", "lastname":"Donkey", "email": "dickd@dd.com",
            "password":"hunter123","city":"Milan","country":"Italy",
            "speaks":"italian","practices":"burmese"
        },

        {
            "firstname": "Nay Min", "lastname": "Htet", "email": "naymin@htet.com",
            "password": "hunter123", "city": "Mandalay", "country": "Myanmar",
            "speaks":"burmese","practices":"italian"
        },

    ]

        for user in user_list:
        speaks = Language.objects.get(LanguageName = user["speaks"])
        practices = Language.objects.get(LanguageName = user["practices"])
        add_user(user["firstname"],user["lastname"],user["email"],user["password"],user["city"],user["country"],
                 speaks, practices)
    '''





def add_Language(name):
    l = Language.objects.get_or_create(LanguageName = name)[0]
    l.save()
    return l
'''
def add_user(firstname,lastname,email,password,city,country,speaks,practices):

    #user = User.objects.create_user(first_name = firstname, last_name = lastname, email = email,
                                    #password = password,city = city, country = country, speaks = speaks, practices = practices)
    #user = UserProfile.objects.get_or_create(first_name = firstname, last_name = lastname,
                                             #email = email, password = password, city = city,
                                             #country = country, speaks = speaks,
                                             #practices = practices)[0]
    print(user)
    user.save()
    return user

'''


if __name__ == '__main__':
    print("Starting Rango population script")
    populate()