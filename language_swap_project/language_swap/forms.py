from django import forms
from django.contrib.auth.models import User
from language_swap.models import UserProfile, Language
from registration.forms import RegistrationForm
from language_swap.helperFunctions import getUserAge, placesReverseGeocoder

class UserRegistrationForm(RegistrationForm):
    username = forms.CharField(max_length=150, required=False, widget=forms.HiddenInput())

    # Extra fields
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    city = forms.CharField(max_length=120, required=False, widget=forms.HiddenInput())
    country = forms.CharField(max_length=120, required=False, widget=forms.HiddenInput())
    places = forms.CharField(widget=forms.TextInput(attrs={'id':'gMapsAutocomplete'}))
    speaks = forms.ModelMultipleChoiceField(queryset=Language.objects.all().order_by('LanguageName'))
    practices = forms.ModelMultipleChoiceField(queryset=Language.objects.all().order_by('LanguageName'))
    gender = forms.ChoiceField(widget=forms.RadioSelect, choices=[("male","Male"), ("female", "Female"), ("other","Other")])
    dob = forms.DateField()

    # Sets username to given email
    def clean_email(self):
        email = self.cleaned_data['email']
        self.cleaned_data['username'] = email
        return email

    def clean_dob(self):
        dob = self.cleaned_data['dob']
        if getUserAge(dob)<13:
            raise forms.ValidationError(u'To create an account you must be at least 13 years old.')
        return dob

    def clean_places(self):
        places = self.cleaned_data['places']
        user_loc = placesReverseGeocoder(places)

        # If the function returns True, sets the city and the country
        # Otherwise generates an error
        if user_loc['status']:
            self.cleaned_data['city'] = user_loc['city'].lower()
            self.cleaned_data['country'] = user_loc['country'].lower()
        else:
            raise forms.ValidationError(u'An error has occurred while fetching the places. Please try again')

class EditProfileForm(forms.ModelForm):
    places = forms.CharField(widget=forms.TextInput(attrs={'id': 'gMapsAutocomplete'}))

    class Meta:
        model = UserProfile
        fields = ('picture','hobby','places')
        exclude = ('first_name','last_name','username','password','email')

    def clean_places(self):
        places = self.cleaned_data['places']
        user_loc = placesReverseGeocoder(places)

        # If the function returns True, sets the city and the country
        # Otherwise generates an error
        if user_loc['status']:
            self.cleaned_data['city'] = user_loc['city'].lower()
            self.cleaned_data['country'] = user_loc['country'].lower()
        else:
            raise forms.ValidationError(u'An error has occurred while fetching the places. Please try again')

class DeleteAccountForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ()
