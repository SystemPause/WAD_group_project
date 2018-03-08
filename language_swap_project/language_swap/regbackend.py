from registration.backends.simple.views import RegistrationView
from language_swap.forms import UserRegistrationForm
from language_swap.models import UserProfile

class MyRegistrationView(RegistrationView):

    form_class = UserRegistrationForm

    def register(self, form_class):
        new_user = super(MyRegistrationView, self).register(form_class)
        first_name = form_class.cleaned_data['first_name']
        last_name = form_class.cleaned_data['last_name']
        #city = form_class.cleaned_data['city']
        #country = form_class.cleaned_data['country']
        #speaks = form_class.cleaned_data['speaks']
        #practices = form_class.cleaned_data['practices']
        new_user.first_name = first_name
        new_user.last_name = last_name
        #new_profile = UserProfile.objects.create(user=new_user, city=city, country=country, speaks=speaks, practices=practices)
        #new_profile.save()
        return new_user

    # Redirects the user to the index page, if successful at logging in
    def get_success_url(self, user):
        return '/LanguageSwap/'