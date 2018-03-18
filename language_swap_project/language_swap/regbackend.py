from registration.backends.simple.views import RegistrationView
from language_swap.forms import UserRegistrationForm
from language_swap.models import UserProfile, Language

class MyRegistrationView(RegistrationView):

    form_class = UserRegistrationForm

    def register(self, form_class):
        if form_class.is_valid():
            new_user = super(MyRegistrationView, self).register(form_class)
            first_name = form_class.cleaned_data['first_name']
            last_name = form_class.cleaned_data['last_name']
            city = form_class.cleaned_data['city']
            country = form_class.cleaned_data['country']
            speaks = form_class.cleaned_data['speaks']
            practices = form_class.cleaned_data['practices']
            gender = form_class.cleaned_data['gender']
            dob = form_class.cleaned_data['dob']
            new_user.first_name = first_name
            new_user.last_name = last_name
            new_user.save()
            new_profile = UserProfile.objects.create(user=new_user, city=city, country=country, gender = gender, dob = dob)
            for language in speaks:
                nlanguage = Language.objects.get(LanguageName=language)
                new_profile.speaks.add(nlanguage)
            for language in practices:
                planguage = Language.objects.get(LanguageName=language)
                new_profile.practices.add(planguage)
            new_profile.save()
            return new_user

    # Redirects the user to the index page, if successful at logging in
    def get_success_url(self, user):
        return '/LanguageSwap/'