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
            speaks = form_class.cleaned_data['speaks'].lower()
            practices = form_class.cleaned_data['practices'].lower()
            gender = form_class.cleaned_data['gender'].lower()
            dob = form_class.cleaned_data['dob']
            new_user.first_name = first_name
            new_user.last_name = last_name
            new_profile = UserProfile.objects.create(user=new_user, city=city, country=country, gender = gender, dob = dob)
            # Only works if given language is in the database
            nlanguage = Language.objects.get(LanguageName=speaks)
            planguage = Language.objects.get(LanguageName=practices)
            new_profile.speaks.add(nlanguage)
            new_profile.practices.add(planguage)
            new_profile.save()
            return new_user

    # Redirects the user to the index page, if successful at logging in
    def get_success_url(self, user):
        return '/LanguageSwap/'