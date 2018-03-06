from django import forms
from language_swap.models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('city', 'country', 'picture', 'hobby', 'speaks', 'practises')