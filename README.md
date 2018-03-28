# LanguageSwap 
## Group Project: WAD2 - University of Glasgow 2018
## Group members: 

 1. Martina Cocco - 2267320C
 2. Zay Yar Tun - 2277073Z
 3. Gloria Dhandapani - 2252533D
 4. Alessandro Speggiorin - 2268690S

## Guide to Website
Welcome to LanguageSwap, a web application where you can find people to exchange and practice new languages.
In the main page, you can search for users who are practicing your native language and fluently speak the language you want to practice
in a particular city without an account. There are over 7000 languages but we have included the most commonly used 
ones (that are available on Google Translate). For the city input, a Google Map API is used and the autocomplete 
function should make the selection easier and to prevent and typos resulting in a smoother process.

But first, to generate sample users, a population script is given to be executed. For optimal users result,
it is recommended that you input "English" as your native language, "Italian" as your practicing language and 
"Milan, Italy" as your city. (Pretend you are an English speaker who wants to practice Italian as you are going to be 
living in Milan). Feel free to test other inputs.

Now you got your users and in order to be able to contact these users, first create an account. The live checking 
registration form should aid you in your account creation.

Once you have gotten an account, you are able to view your profile which contains your main information and from the 
profile page, you are able to edit those information, change password and if needed, delete your account. If you forgot 
your password, there is a feature to reset it.

Next, you have to modify settings.py,set username and password fields to what is given in the project summary (stated there to 
not make the info public). Then you are able to contact the users. The contacting system is designed so that the message will be sent 
to the other user's email inbox where the message sender will be our website's email. The actual sender's information will 
be presented in the email title.

All the users you have contacted will appear on your contact history where you can rate each user on a scale of 1 to 5. 
We have made sure that once you have rated, you wont have to refresh the page to see the changes.

The page is made responsive and adaptable to changes so feel free to resize your browser or access it from your phone.

## Languages Supported
Afrikaans, Albanian, Amharic, Arabic, Armenian, Azerbaijani, Basque, Belarusian, Bengali, Bosnian, Bulgarian, Burmese, Catalan, Cebuano, Chichewa, Chinese, Corsican, Croatian, Czech, Danish, Dutch, English, Esperanto, Estonian, Filipino, Finnish, French, Frisian, Gaelic, Galician, Georgian, German, Greek, Gujarati, Haitian, Hausa, Hawaiian, Hebrew, Hindi, Hmong, Hungarian, Icelandic, Igbo, Indonesian, Irish, Italian, Japanese, Javanese, Kannada, Kazakh, Khmer, Korean, Kurdish, Kyrgyz, Lao, Latin, Latvian, Lithuanian, Luxembourgish, Macedonian, Malagasy, Malay, Malayalam, Maltese, Maori, Marathi, Mongolian, Nepali, Norwegian, Pashto, Persian, Polish, Portuguese, Punjabi, Romanian, Russian, Samoan, Serbian, Sesotho, Shona, Sindhi, Sinhala, Slovak, Slovenian, Somali, Spanish, Sundanese, Swahili, Swedish, Tajik, Tamil, Telugu, Thai, Turkish, Ukrainian, Urdu, Uzbek, Vietnamese, Welsh, Xhosa, Yiddish, Yoruba, Zulu


## External Sources
*	Google Map API (https://developers.google.com/maps/documentation/javascript/places-autocomplete & https://developers.google.com/maps/documentation/geocoding/intro)
*	Bootstrap (https://getbootstrap.com/)
*	Requests (http://docs.python-requests.org/en/master/user/quickstart/)
*	jQuery (https://jquery.com/)
*	Font Awesome (https://fontawesome.com/)
*	Gmail (https://mail.google.com/)
*	Django registration redux (https://django-registration-redux.readthedocs.io/en/latest/)
*	Select2 (https://select2.org)
For Presentation
*	Hislide (https://hislide.io/)
*	Carbon (https://carbon.now.sh)
*	Smartmockups (https://smartmockups.com/)


