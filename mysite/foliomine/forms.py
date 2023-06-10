from .models import Profile, Experience, Project, Education
from django import forms


class CreateProfileForm(forms.ModelForm):

    profile_name = forms.CharField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    about = forms.CharField(widget=forms.Textarea())
    github_link = forms.CharField()
    linkedin_link = forms.CharField()
    profile_photo = forms.FileField(required=False)

    class Meta:
        model = Profile
        fields = ('profile_name',
                  'first_name',
                  'last_name',
                  'about',
                  'github_link',
                  'twitter_link',
                  'linkedin_link',
                  'profile_photo')


class CreateExperienceForm(forms.ModelForm):

    company_name = forms.CharField(widget=forms.TextInput(),
                                   label='Company Name')
    job_profile = forms.CharField(widget=forms.TextInput(),
                                  label='Job Profile')
    exp_start_date = forms.DateField(widget=forms.DateInput(), label='Start Date')
    exp_end_date = forms.DateField(widget=forms.DateInput(), label='End Date')
    details = forms.CharField(widget=forms.Textarea(), label='Description')

    class Meta:
        model = Experience
        fields = ('company_name',
                  'exp_start_date',
                  'exp_end_date',
                  'details',
                  'job_profile')


class CreateProjectForm(forms.ModelForm):

    project_name = forms.CharField(widget=forms.TextInput(
        attrs={"class": "folio-form-input cols-span-2"}), label='Project Name')
    proj_start_date = forms.DateField(
        input_formats=['%m-%Y'], label='Start Date')
    proj_end_date = forms.DateField(input_formats=['%m-%Y'],
                               widget=forms.DateInput(), label='End Date')
    project_details = forms.CharField(widget=forms.Textarea())
    project_link = forms.CharField(label='Project Link')
    project_code_link = forms.CharField(label='Code Link')
    project_photo = forms.FileField(required=False, label='Project Snapshot')

    class Meta:
        model = Project
        fields = ('project_name',
                  'proj_start_date',
                  'proj_end_date',
                  'project_details',
                  'project_link',
                  'project_code_link',
                  'project_photo')


class CreateEducationForm(forms.ModelForm):

    edu_end_date = forms.DateField(input_formats=['%m-%Y'], label='End Date')
    school = forms.CharField(label='School Name')
    degree = forms.CharField(label='Degree')
    city = forms.CharField(label='City')
    country = forms.CharField(label='Country')
    grade = forms.CharField(label='Grade')

    class Meta:
        model = Education
        fields = (
            'school',
            'edu_end_date',
            'degree',
            'city',
            'country',
            'grade'
        )
