from django import forms
from django.contrib.auth.models import User
from language_swap.models import UserProfile, Language
from registration.forms import RegistrationForm
from language_swap.helperFunctions import getUserAge

class UserRegistrationForm(RegistrationForm):
    username = forms.CharField(max_length=150, required=False, widget=forms.HiddenInput())

    # Extra fields
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=150)
    city = forms.CharField(max_length=120)
    country = forms.CharField(max_length=120)
    speaks = forms.ModelMultipleChoiceField(queryset=Language.objects.all().order_by('LanguageName'))
    practices = forms.ModelMultipleChoiceField(queryset=Language.objects.all().order_by('LanguageName'))
    gender = forms.CharField(max_length=10)
    dob = forms.DateField()

    # Sets username to given email
    def clean_email(self):
        email = self.cleaned_data['email']
        if email and User.objects.filter(email=email).exists():
            raise forms.ValidationError('This email address is already in use. Please supply a different email address.')
        self.cleaned_data['username'] = email
        return email

    def clean_dob(self):
        dob = self.cleaned_data['dob']
        if getUserAge(dob)<13:
            raise forms.ValidationError('To create an account you must be at least 13 years old.')
        return dob

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('city', 'country', 'picture', 'hobby', 'speaks', 'practices')