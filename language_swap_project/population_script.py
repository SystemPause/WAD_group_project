import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'language_swap_project.settings')

import django
django.setup()
from language_swap.models import UserProfile,Language,Contact,User
import pycountry

def populate():
    language_list = ["italian", "french", "burmese", "english", "spanish","mandarin","german","japanese","korean","indian"]
    for lang in language_list:
        add_Language(lang)
    '''
    for language in pycountry.languages:
        language_list.append(language.name.lower())
        add_Language(language.name.lower())
    '''



    user_list = [
        {
            "firstname": "Dicky", "lastname":"Donkey","username":"dickd@dd.com", "email": "dickd@dd.com",
            "password":"hunter123","city":"milan","country":"italy", "gender":"female","dob":"1995-02-03",
            "speaks":["italian","french"],"practices":["burmese","english"]
        },

        {
            "firstname": "Nay Min", "lastname": "Htet","username":"naymin@htet.com", "email": "naymin@htet.com",
            "password": "hunter123", "city": "milan", "country": "italy","gender":"male","dob":"1995-12-15",
            "speaks":["burmese","italian"],"practices":["italian","english"]
        },
        
        {
            "firstname": "Dante", "lastname":"The little pigeon","username":"yolo@dd.com", "email": "yolo@dd.com",
            "password":"hunter123","city":"milan","country":"italy","gender":"male","dob":"1992-01-26",
            "speaks":["italian","french"],"practices":["burmese","english"]
        },

        {
            "firstname": "Mister", "lastname": "Man", "username": "mister@mister.com", "email": "mister@mister.com",
            "password": "hunter123", "city": "milan", "country": "italy", "gender": "male", "dob": "1991-04-06",
            "speaks": ["italian", "burmese"], "practices": ["japanese", "english"]
        },

        {
            "firstname": "Lee", "lastname": "Sook", "username": "leesook@kmail.com", "email": "leesook@kmail.com",
            "password": "hunter123", "city": "seoul", "country": "korea", "gender": "female", "dob": "1996-05-05",
            "speaks": ["korean", "english"], "practices": ["french", "italian"]
        },
        {
            "firstname": "Wang", "lastname": "Huang", "username": "whuang@cmail.com", "email": "whuang@cmail.com",
            "password": "hunter123", "city": "shenzhen", "country": "china", "gender": "female", "dob": "1992-04-15",
            "speaks": ["mandarin", "french"], "practices": ["burmese", "english"]
        },
        {
            "firstname": "Ramesh", "lastname": "Ali", "username": "mali@mail.com", "email": "mali@mail.com",
            "password": "hunter123", "city": "bombay", "country": "india", "gender": "male", "dob": "1996-08-26",
            "speaks": ["indian", "english"], "practices": ["spanish", "korean"]
        },
        {
            "firstname": "Santiago", "lastname": "Lopez", "username": "slopez@hotmail.com", "email": "slopez@hotmail.com",
            "password": "hunter123", "city": "barcelona", "country": "spain", "gender": "male", "dob": "1992-01-15",
            "speaks": ["spanish", "italian"], "practices": ["english", "french"]
        },
        {
            "firstname": "Xiao", "lastname": "Qi", "username": "xxq@cmail.com", "email": "xxq@cmail.com",
            "password": "hunter123", "city": "shanghai", "country": "china", "gender": "female", "dob": "1995-02-10",
            "speaks": ["mandarin", "english"], "practices": ["korean", "japanese"]
        },
        {
            "firstname": "Hanada", "lastname": "Shiro", "username": "hana@jmail.com", "email": "hana@jmail.com",
            "password": "hunter123", "city": "osaka", "country": "japan", "gender": "female", "dob": "1994-12-12",
            "speaks": ["japanese", "english"], "practices": ["french", "burmese"]
        },
        {
            "firstname": "Aung", "lastname": "Min", "username": "amin@mail.com", "email": "amin@mail.com",
            "password": "hunter123", "city": "yangon", "country": "myanmar", "gender": "male", "dob": "1992-03-15",
            "speaks": ["burmese", "english"], "practices": ["indian", "mandarin"]
        },
        {
            "firstname": "Tomo", "lastname": "Naka", "username": "tnaka@jmail.com", "email": "tnaka@jmail.com",
            "password": "hunter123", "city": "tokyo", "country": "japan", "gender": "female", "dob": "1991-04-26",
            "speaks": ["japanese", "french"], "practices": ["english", "italian"]
        },
        {
            "firstname": "Hyun", "lastname": "Jun", "username": "jun@kmail.com", "email": "jun@kmail.com",
            "password": "hunter123", "city": "seoul", "country": "korea", "gender": "female", "dob": "1993-06-15",
            "speaks": ["korean", "mandarin"], "practices": ["indian", "english"]
        },
        {
            "firstname": "Muhammad", "lastname": "Muhammad", "username": "mm@mail.com", "email": "mm@mail.com",
            "password": "hunter123", "city": "new dehli", "country": "india", "gender": "male", "dob": "1994-01-01",
            "speaks": ["indian", "english"], "practices": ["mandarin", "italian"]
        },
        {
            "firstname": "Fernandez", "lastname": "Garcia", "username": "fg@cmail.com", "email": "fg@cmail.com",
            "password": "hunter123", "city": "madrid", "country": "spain", "gender": "male", "dob": "1995-04-28",
            "speaks": ["spanish", "italian"], "practices": ["burmese", "korean"]
        },
        {
            "firstname": "Lao", "lastname": "You", "username": "ly@cmail.com", "email": "ly@cmail.com",
            "password": "hunter123", "city": "beijing", "country": "china", "gender": "male", "dob": "1993-06-14",
            "speaks": ["mandarin", "english","french"], "practices": ["burmese", "italian"]
        },
        {
            "firstname": "Alessandro", "lastname": "Speggy", "username": "ass@cmail.com", "email": "ass@cmail.com",
            "password": "hunter123", "city": "vicenza", "country": "italy", "gender": "female", "dob": "1996-11-11",
            "speaks": ["italian", "mandarin"], "practices": ["indian", "japanese"]
        },
        {
            "firstname": "Sebastian", "lastname": "Thomas", "username": "sbtms@cmail.com", "email": "sbtms@cmail.com",
            "password": "hunter123", "city": "paris", "country": "france", "gender": "male", "dob": "1994-01-15",
            "speaks": ["english", "french"], "practices": ["burmese", "italian"]
        },
        {
            "firstname": "Giovanni", "lastname": "Toti", "username": "gtoti@cmail.com", "email": "gtoti@cmail.com",
            "password": "hunter123", "city": "tuscany", "country": "italy", "gender": "male", "dob": "1996-02-20",
            "speaks": ["italian", "french"], "practices": ["spanish", "english"]
        },
        {
            "firstname": "Hua", "lastname": "Lin", "username": "hlin@cmail.com", "email": "hlin@cmail.com",
            "password": "hunter123", "city": "shenzhen", "country": "china", "gender": "female", "dob": "1995-02-10",
            "speaks": ["mandarin", "english"], "practices": ["burmese", "korean","japanese"]
        },
        {
            "firstname": "Marti", "lastname": "Smarti", "username": "marti@cmail.com", "email": "marti@cmail.com",
            "password": "hunter123", "city": "vicenza", "country": "italy", "gender": "female", "dob": "1996-01-29",
            "speaks": ["italian", "english"], "practices": ["french", "japanese", "spanish"]
        },
        {
            "firstname": "Park", "lastname": "Hyun", "username": "phyu@cmail.com", "email": "phyu@cmail.com",
            "password": "hunter123", "city": "seoul", "country": "korea", "gender": "male", "dob": "1993-01-20",
            "speaks": ["korean", "indian"], "practices": ["english", "mandarin"]
        },
        {
            "firstname": "Tom", "lastname": "Yum", "username": "tomy@cmail.com", "email": "tomy@cmail.com",
            "password": "hunter123", "city": "london", "country": "united kingdom", "gender": "male", "dob": "1996-02-21",
            "speaks": ["english"], "practices": ["italian", "mandarin"]
        },
        {
            "firstname": "Beer", "lastname": "Man", "username": "bman@cmail.com", "email": "bman@cmail.com",
            "password": "hunter123", "city": "london", "country": "united kingdom", "gender": "male", "dob": "1994-01-04",
            "speaks": ["english", "french"], "practices": ["mandarin", "burmese"]
        },
        {
            "firstname": "Shido", "lastname": "Yama", "username": "shy@cmail.com", "email": "shy@cmail.com",
            "password": "hunter123", "city": "kyoto", "country": "japan", "gender": "male", "dob": "1994-01-21",
            "speaks": ["japanese", "korean"], "practices": ["mandarin", "english"]
        },
        {
            "firstname": "Mandy", "lastname": "Blanc", "username": "mandy@cmail.com", "email": "mandy@cmail.com",
            "password": "hunter123", "city": "paris", "country": "france", "gender": "female", "dob": "1991-01-25",
            "speaks": ["italian", "french"], "practices": ["english", "indian"]
        },
        {
            "firstname": "Howard", "lastname": "Lance", "username": "hlance@cmail.com", "email": "hlance@cmail.com",
            "password": "hunter123", "city": "glasgow", "country": "united kingdom", "gender": "male", "dob": "1992-05-05",
            "speaks": ["english"], "practices": ["french", "italian"]
        },
        {
            "firstname": "Min", "lastname": "Min", "username": "mm@cmail.com", "email": "mm@cmail.com",
            "password": "hunter123", "city": "yangon", "country": "myanmar", "gender": "male", "dob": "1994-07-20",
            "speaks": ["burmese", "mandarin"], "practices": ["english", "italian"]
        },
        {
            "firstname": "Gloria", "lastname": "DaMan", "username": "gloman@cmail.com", "email": "gloman@cmail.com",
            "password": "hunter123", "city": "manchester", "country": "united kingdom", "gender": "female", "dob": "1991-04-06",
            "speaks": ["english", "indian"], "practices": ["italian", "spanish"]
        },
        {
            "firstname": "Louis", "lastname": "Ville", "username": "lvi@cmail.com", "email": "lvi@cmail.com",
            "password": "hunter123", "city": "toulouse", "country": "france", "gender": "male", "dob": "1993-02-20",
            "speaks": ["italian", "french"], "practices": ["spanish", "english"]
        },
        {
            "firstname": "Vim", "lastname": "Wandauandslfeseee", "username": "wim@cmail.com", "email": "wim@cmail.com",
            "password": "hunter123", "city": "glasgow", "country": "united kingdom", "gender": "other", "dob": "1988-01-01",
            "speaks": ["english", "japanese"], "practices": ["japanese", "mandarin"]
        },
    ]
    
    for user in user_list:
        speaksList = []

        for sth in user["speaks"]:
            speaksList.append(Language.objects.get(LanguageName = sth))


        practicesList = []

        for sth in user["practices"]:
            practicesList.append(Language.objects.get(LanguageName=sth))


        add_user(user["firstname"],user["lastname"],user["username"],user["email"],user["password"],user["city"],
                 user["country"],user["gender"],user["dob"],speaksList,practicesList)


def add_Language(name):
    l = Language.objects.get_or_create(LanguageName = name)[0]
    l.save()
    return l

def add_user(firstname,lastname,username,email,password,city,country,gender,dob,speaks,practices):

    userObject = User.objects.get_or_create(first_name = firstname, last_name = lastname,username =username,  email = email,
                                    password = password)[0]
    userObject.set_password(userObject.password)
    userObject.save()



    userProfile = UserProfile.objects.get_or_create(user = userObject, city = city,
                                             country = country,gender = gender, dob = dob)[0]
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