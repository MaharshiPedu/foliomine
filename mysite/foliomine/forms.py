from .models import Profile, Experience
from django import forms


class CreateProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ('profile_name', 'first_name', 'last_name', 'about',
                  'github_link', 'twitter_link', 'linkedin_link', 'profile_photo')
        labels = {'profile_name': 'Profile Name', 'first_name': 'First Name', 'last_name': 'Last Name',     'about': 'About','github_link': 'GitHub Link', 'twitter_link': 'Twitter Link', 'linkedin_link': 'LinkedIn Link', 'profile_photo': 'Profile img'}
    
    class Meta:
        model = Experience
        fields = ('company_name', 'start_date', 'end_date', 'details', 'job_profile')
        labels = {'company_name':'Company Name', 'start_date':'Start Date', 'end_date':'End Date', 
                  'details':'Description', 'job_profile':'Job Profile'}