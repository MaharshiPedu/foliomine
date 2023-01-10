from .models import Profile
from django import forms


class CreateProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'about',
                  'github_link', 'twitter_link', 'linkedin_link', 'profile_photo')
        labels = {'first_name': 'First Name', 'last_name': 'Last Name', 'about': 'About',
                  'github_link': 'GitHub Link', 'twitter_link': 'Twitter Link', 'linkedin_link': 'LinkedIn Link', 'profile_photo':'Profile img'}
