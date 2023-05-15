from .models import Profile, Experience
from django import forms

class CreateProfileForm(forms.ModelForm):

    profile_name = forms.CharField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    about = forms.CharField(widget=forms.Textarea(attrs={
        "class":"w-full rounded-lg border-4 border-[#004aad] bg-website_blue text-label_white"}))
    github_link = forms.CharField()
    linkedin_link = forms.CharField()
    profile_photo = forms.FileField()

    class Meta:
        model = Profile
        fields = ('profile_name', 'first_name', 'last_name', 'about',
                  'github_link', 'twitter_link', 'linkedin_link', 'profile_photo')
        # labels = {'profile_name': 'Profile Name', 'first_name': 'First Name',
                    #'last_name': 'Last Name',     'about': 'About',
                    #'github_link': 'GitHub Link', 'twitter_link': 'Twitter Link',
                    #'linkedin_link': 'LinkedIn Link', 'profile_photo': 'Profile img'}

class CreateExperienceForm(forms.ModelForm):

    company_name = forms.CharField(widget = forms.TextInput(attrs={"class":"folio-form-input cols-span-2"}))
    job_profile = forms.CharField(widget = forms.TextInput(attrs={"class":"folio-form-input cols-span-2"}))
    start_date = forms.DateField(widget = forms.DateInput(attrs={"type":"date", "class":"folio-form-input cols-span-2"}))
    end_date = forms.DateField(widget = forms.DateInput(attrs={"type":"date", "class":"folio-form-input cols-span-2"}))
    details = forms.CharField(widget = forms.Textarea(attrs={"class":"w-full rounded-lg border-4 border-[#004aad] bg-website_blue text-label_white"}))

    class Meta:
        model = Experience
        fields = ('company_name', 'job_profile', 'start_date', 'end_date', 'details')
        labels = {'company_name':'Company Name', 'job_profile':'Job Profile',
                'start_date':'Start Date', 'end_date':'End Date',
                'details':'Description'}
