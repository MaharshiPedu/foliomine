from .models import Profile
from django import forms


class CreateProfileForm(forms.Form):

    first_name    = forms.CharField(max_length=25)
    last_name     = forms.CharField(max_length=25)
    about         = forms.CharField(max_length=500, widget=forms.Textarea)
    #profile_photo = forms.ImageField(upload_to='profile_photos/%Y/%m/%d/', blank=True, null=True)
    github_link   = forms.URLField(max_length=250, required=False) 
    twitter_link  = forms.URLField(max_length=250, required=False) 
    linkedin_link = forms.URLField(max_length=250, required=False)

    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'about', 'github_link')
