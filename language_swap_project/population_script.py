import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'language_swap_project.settings')

import django
django.setup()
from language_swap.models import UserProfile,Language,Contact,User

def populate():
    #populate languages first, neccessary since language objects are needed in "speaks" and "practices" fields of user
    language_list = ["afrikaans","albanian","amharic","arabic","armenian","azerbaijani","basque","belarusian","bengali",
                     "bosnian","bulgarian","burmese","catalan","cebuano","chichewa","chinese","corsican","croatian",
                     "czech","danish","dutch","english","esperanto","estonian","filipino","finnish","french","frisian",
                     "gaelic","galician","georgian","german","greek","gujarati","haitian","hausa","hawaiian","hebrew",
                     "hindi","hmong","hungarian","icelandic","igbo","indonesian","irish","italian","japanese","javanese",
                     "kannada","kazakh","khmer","korean","kurdish","kyrgyz","lao","latin","latvian","lithuanian",
                     "luxembourgish","macedonian","malagasy","malay","malayalam","maltese","maori","marathi","mongolian",
                     "nepali","norwegian","pashto","persian","polish","portuguese","punjabi","romanian","russian",
                     "samoan","serbian","sesotho","shona","sindhi","sinhala","slovak","slovenian","somali","spanish",
                     "sundanese","swahili","swedish","tajik","tamil","telugu","thai","turkish","ukrainian","urdu",
                     "uzbek","vietnamese","welsh","xhosa","yiddish","yoruba","zulu"]
    for lang in language_list:
        add_Language(lang)


    user_list = [
        {
            "firstname": "Marco", "lastname":"Bianchi","username":"marh@gmx.com", "email": "marh@gmx.com",
            "password":"hunter123","city":"milan","country":"italy", "gender":"male","dob":"1995-02-03",
            "speaks":["italian","french"],"practices":["spanish","english"],"image":"profile_images/marco.jpeg",
            "hobby":"I am a very nurturing person and I teach maths"
        },

        {
            "firstname": "Giulia", "lastname": "Ricci","username":"naymin@gmx.com", "email": "naymin@gmx.com",
            "password": "hunter123", "city": "milan", "country": "italy","gender":"female","dob":"1995-12-15",
            "speaks":["burmese","italian"],"practices":["french","english"],"image":"profile_images/giulia.jpeg",
            "hobby":"I like painting and playing piano"
        },

        {
            "firstname": "Luca", "lastname":"Ferrari","username":"yolo@gmx.com", "email": "yolo@gmx.com",
            "password":"hunter123","city":"milan","country":"italy","gender":"male","dob":"1992-01-26",
            "speaks":["italian","french"],"practices":["burmese","english"],"image":"profile_images/luca.jpeg",
            "hobby":"I like playing football and to watch football and to feel the football"
        },

        {
            "firstname": "Giovanni", "lastname": "Gallo", "username": "mister@gmx.com", "email": "mister@gmx.com",
            "password": "hunter123", "city": "milan", "country": "italy", "gender": "male", "dob": "1991-04-06",
            "speaks": ["italian", "burmese"], "practices": ["japanese", "english"],"image":"profile_images/giovanni.jpeg",
            "hobby":"I am a chef and I cook amazing food"
        },

        {
            "firstname": "Elena", "lastname": "Rizzo", "username": "elena@gmx.com", "email": "elena@gmx.com",
            "password": "hunter123", "city": "milan", "country": "italy", "gender": "female", "dob": "1996-05-05",
            "speaks": ["italian", "chinese"], "practices": ["english", "japanese"],"image":"profile_images/elena.jpeg",
            "hobby":"I like asia"
        },
        {
            "firstname": "Wang", "lastname": "Huang", "username": "whuang@gmx.com", "email": "whuang@gmx.com",
            "password": "hunter123", "city": "shenzhen", "country": "china", "gender": "female", "dob": "1992-04-15",
            "speaks": ["chinese", "french"], "practices": ["burmese", "english"],"image":"",
            "hobby":""
        },
        {
            "firstname": "Ramesh", "lastname": "Ali", "username": "mali@gmx.com", "email": "mali@gmx.com",
            "password": "hunter123", "city": "mumbai", "country": "india", "gender": "male", "dob": "1996-08-26",
            "speaks": ["hindi", "english"], "practices": ["spanish", "korean"],"image":"",
            "hobby":""
        },
        {
            "firstname": "Santiago", "lastname": "Lopez", "username": "slopez@gmx.com", "email": "slopez@gmx.com",
            "password": "hunter123", "city": "barcelona", "country": "spain", "gender": "male", "dob": "1992-01-15",
            "speaks": ["spanish", "italian"], "practices": ["english", "french"],"image":"",
            "hobby":""
        },
        {
            "firstname": "Xiao", "lastname": "Qi", "username": "xxq@gmx.com", "email": "xxq@gmx.com",
            "password": "hunter123", "city": "shanghai", "country": "china", "gender": "female", "dob": "1995-02-10",
            "speaks": ["chinese", "english"], "practices": ["korean", "japanese"],"image":"",
            "hobby":""
        },
        {
            "firstname": "Hanada", "lastname": "Shiro", "username": "hana@gmx.com", "email": "hana@gmx.com",
            "password": "hunter123", "city": "osaka", "country": "japan", "gender": "female", "dob": "1994-12-12",
            "speaks": ["japanese", "english"], "practices": ["french", "burmese"],"image":"",
            "hobby":""
        },
        {
            "firstname": "Aung", "lastname": "Min", "username": "amin@gmx.com", "email": "amin@gmx.com",
            "password": "hunter123", "city": "yangon", "country": "myanmar", "gender": "male", "dob": "1992-03-15",
            "speaks": ["burmese", "english"], "practices": ["hindi", "chinese"],"image":"",
            "hobby":""
        },
        {
            "firstname": "Tomo", "lastname": "Naka", "username": "tnaka@gmx.com", "email": "tnaka@gmx.com",
            "password": "hunter123", "city": "tokyo", "country": "japan", "gender": "female", "dob": "1991-04-26",
            "speaks": ["japanese", "french"], "practices": ["english", "italian"],"image":"",
            "hobby":""
        },
        {
            "firstname": "Hyun", "lastname": "Jun", "username": "jun@gmx.com", "email": "jun@gmx.com",
            "password": "hunter123", "city": "seoul", "country": "south korea", "gender": "female", "dob": "1993-06-15",
            "speaks": ["korean", "chinese"], "practices": ["hindi", "english"],"image":"",
            "hobby":""
        },
        {
            "firstname": "Muhammad", "lastname": "Muhammad", "username": "mm@gmx.com", "email": "mm@gmx.com",
            "password": "hunter123", "city": "new dehli", "country": "india", "gender": "male", "dob": "1994-01-01",
            "speaks": ["hindi", "english"], "practices": ["chinese", "italian"],"image":"",
            "hobby":""
        },
        {
            "firstname": "Fernandez", "lastname": "Garcia", "username": "fg@gmx.com", "email": "fg@gmx.com",
            "password": "hunter123", "city": "madrid", "country": "spain", "gender": "male", "dob": "1995-04-28",
            "speaks": ["spanish", "italian"], "practices": ["burmese", "korean"],"image":"",
            "hobby":""
        },
        {
            "firstname": "Lao", "lastname": "You", "username": "ly@gmx.com", "email": "ly@gmx.com",
            "password": "hunter123", "city": "beijing", "country": "china", "gender": "male", "dob": "1993-06-14",
            "speaks": ["chinese", "english","french"], "practices": ["burmese", "italian"],"image":"",
            "hobby":""
        },
        {
            "firstname": "Alessandro", "lastname": "Speggy", "username": "ass@gmx.com", "email": "ass@gmx.com",
            "password": "hunter123", "city": "vicenza", "country": "italy", "gender": "female", "dob": "1996-11-11",
            "speaks": ["italian", "chinese"], "practices": ["hindi", "japanese"],"image":"",
            "hobby":""
        },
        {
            "firstname": "Sebastian", "lastname": "Thomas", "username": "sbtms@gmx.com", "email": "sbtms@gmx.com",
            "password": "hunter123", "city": "paris", "country": "france", "gender": "male", "dob": "1994-01-15",
            "speaks": ["english", "french"], "practices": ["burmese", "italian"],"image":"",
            "hobby":""
        },
        {
            "firstname": "Giovanni", "lastname": "Toti", "username": "gtoti@gmx.com", "email": "gtoti@gmx.com",
            "password": "hunter123", "city": "florence", "country": "italy", "gender": "male", "dob": "1996-02-20",
            "speaks": ["italian", "french"], "practices": ["spanish", "english"],"image":"",
            "hobby":""
        },
        {
            "firstname": "Hua", "lastname": "Lin", "username": "hlin@gmx.com", "email": "hlin@gmx.com",
            "password": "hunter123", "city": "shenzhen", "country": "china", "gender": "female", "dob": "1995-02-10",
            "speaks": ["chinese", "english"], "practices": ["burmese", "korean","japanese"],"image":"",
            "hobby":""
        },
        {
            "firstname": "Marti", "lastname": "Smarti", "username": "marti@gmx.com", "email": "marti@gmx.com",
            "password": "hunter123", "city": "vicenza", "country": "italy", "gender": "female", "dob": "1996-01-29",
            "speaks": ["italian", "english"], "practices": ["french", "japanese", "spanish"],"image":"",
            "hobby":""
        },
        {
            "firstname": "Park", "lastname": "Hyun", "username": "phyu@gmx.com", "email": "phyu@gmx.com",
            "password": "hunter123", "city": "seoul", "country": "south korea", "gender": "male", "dob": "1993-01-20",
            "speaks": ["korean", "hindi"], "practices": ["english", "chinese"],"image":"",
            "hobby":""
        },
        {
            "firstname": "Tom", "lastname": "Yum", "username": "tomy@gmx.com", "email": "tomy@gmx.com",
            "password": "hunter123", "city": "london", "country": "united kingdom", "gender": "male", "dob": "1996-02-21",
            "speaks": ["english"], "practices": ["italian", "chinese"],"image":"",
            "hobby":""
        },
        {
            "firstname": "Beer", "lastname": "Man", "username": "bman@gmx.com", "email": "bman@gmx.com",
            "password": "hunter123", "city": "london", "country": "united kingdom", "gender": "male", "dob": "1994-01-04",
            "speaks": ["english", "french"], "practices": ["chinese", "burmese"],"image":"",
            "hobby":""
        },
        {
            "firstname": "Shido", "lastname": "Yama", "username": "shy@gmx.com", "email": "shy@gmx.com",
            "password": "hunter123", "city": "kyoto", "country": "japan", "gender": "male", "dob": "1994-01-21",
            "speaks": ["japanese", "korean"], "practices": ["chinese", "english"],"image":"",
            "hobby":""
        },
        {
            "firstname": "Mandy", "lastname": "Blanc", "username": "mandy@gmx.com", "email": "mandy@gmx.com",
            "password": "hunter123", "city": "paris", "country": "france", "gender": "female", "dob": "1991-01-25",
            "speaks": ["italian", "french"], "practices": ["english", "hindi"],"image":"",
            "hobby":""
        },
        {
            "firstname": "Howard", "lastname": "Lance", "username": "hlance@gmx.com", "email": "hlance@gmx.com",
            "password": "hunter123", "city": "glasgow", "country": "united kingdom", "gender": "male", "dob": "1992-05-05",
            "speaks": ["english"], "practices": ["french", "italian"],"image":"",
            "hobby":""
        },
        {
            "firstname": "Min", "lastname": "Min", "username": "min@gmx.com", "email": "min@gmx.com",
            "password": "hunter123", "city": "yangon", "country": "myanmar", "gender": "male", "dob": "1994-07-20",
            "speaks": ["burmese", "chinese"], "practices": ["english", "italian"],"image":"",
            "hobby":""
        },
        {
            "firstname": "Gloria", "lastname": "DaMan", "username": "gloman@gmx.com", "email": "gloman@gmx.com",
            "password": "hunter123", "city": "manchester", "country": "united kingdom", "gender": "female", "dob": "1991-04-06",
            "speaks": ["english", "hindi"], "practices": ["italian", "spanish"],"image":"",
            "hobby":""
        },
        {
            "firstname": "Louis", "lastname": "Ville", "username": "lvi@gmx.com", "email": "lvi@gmx.com",
            "password": "hunter123", "city": "toulouse", "country": "france", "gender": "male", "dob": "1993-02-20",
            "speaks": ["italian", "french"], "practices": ["spanish", "english"],"image":"",
            "hobby":""
        },
        {
            "firstname": "Vim", "lastname": "Wandauandslfeseee", "username": "wim@gmx.com", "email": "wim@gmx.com",
            "password": "hunter123", "city": "glasgow", "country": "united kingdom", "gender": "other", "dob": "1988-01-01",
            "speaks": ["english", "japanese"], "practices": ["japanese", "chinese"],"image":"",
            "hobby":""
        },
    ]

    #language the user speaks and practices are initially strings and must be converted into Language objects
    for user in user_list:
        speaksList = []

        for sth in user["speaks"]:
            speaksList.append(Language.objects.get(LanguageName = sth))


        practicesList = []

        for sth in user["practices"]:
            practicesList.append(Language.objects.get(LanguageName=sth))


        add_user(user["firstname"],user["lastname"],user["username"],user["email"],user["password"],user["city"],
                 user["country"],user["gender"],user["dob"],speaksList,practicesList,user["image"],user["hobby"])


    rateList = [
        {"contacter":"marh@gmx.com", "contactee":"yolo@gmx.com","score":5},
        {"contacter": "yolo@gmx.com", "contactee": "marh@gmx.com", "score": 4},
        {"contacter": "mister@gmx.com", "contactee": "yolo@gmx.com", "score": 4},
        {"contacter": "lvi@gmx.com", "contactee": "yolo@gmx.com", "score": 5},
        {"contacter": "gtoti@gmx.com", "contactee": "yolo@gmx.com", "score": 5},
        {"contacter": "yolo@gmx.com", "contactee": "gtoti@gmx.com", "score": 0},
        {"contacter": "mister@gmx.com", "contactee": "marh@gmx.com", "score": 2},
        {"contacter": "marh@gmx.com", "contactee": "mister@gmx.com", "score": 3},
        {"contacter": "lvi@gmx.com", "contactee": "mister@gmx.com", "score": 2},

    ]
    for contact in rateList:
        #both end users are initially strings so we need to obtain UserProfile object from it
        contacter = UserProfile.objects.get(user = User.objects.get(username = contact["contacter"]))
        contactee = UserProfile.objects.get(user = User.objects.get(username = contact["contactee"]))

        add_contact(contacter,contactee,contact["score"])


def add_Language(name):
    l = Language.objects.get_or_create(LanguageName = name)[0]
    l.save()
    return l

def add_user(firstname,lastname,username,email,password,city,country,gender,dob,speaks,practices,image,hobby):

    userObject = User.objects.get_or_create(first_name = firstname, last_name = lastname,username =username,  email = email,
                                    password = password)[0]
    userObject.set_password(userObject.password)
    userObject.save()

    '''
    in order to add a UserProfile which uses User Model as one of the attributes,
    we must first create a User object then using that User object we create the UserProfile
    '''

    userProfile = UserProfile.objects.get_or_create(user = userObject, city = city,
                                             country = country,gender = gender, dob = dob)[0]
    if image != '':
        userProfile.picture = image

    if hobby !='':
        userProfile.hobby = hobby

    userProfile.save()

    '''
    speaks and practices are many to many fields and since a user can potentially speak more than one language,
    we loop through every language and add them individually to the many to many relationship
    '''
    for sth in speaks:
        userProfile.speaks.add(sth)

    for sth in practices:
        userProfile.practices.add(sth)



    return userObject,userObject

def add_contact(contacter,contactee,score):
    c = Contact.objects.get_or_create(sourceUser = contacter,contactedUser = contactee,score = score)[0]
    c.save()
    return c

if __name__ == '__main__':
    print("Starting LanguageSwap population script")
    populate()
