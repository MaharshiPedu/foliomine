from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import CreateProfileForm, CreateExperienceForm, CreateProjectForm, CreateEducationForm
from .models import Profile, Experience, Project, Education
from json import dumps, JSONEncoder
from datetime import date
from mysite.settings import MEDIA_ROOT

# temporary, just for testing
from django.forms import model_to_dict

def index(request):
    if request.user.is_authenticated:
        user = request.user
        profiles = Profile.objects.filter(user_id=user.id)
        return render(request, 'foliomine/index.html', {'profiles': profiles})

    return render(request, 'foliomine/index.html', {})


@login_required
def create_profile(request):

    if request.method == 'POST':
        form = CreateProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(commit=False)
            profile_name = form.cleaned_data['profile_name']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            about = form.cleaned_data['about']
            github_link = form.cleaned_data['github_link']
            twitter_link = form.cleaned_data['twitter_link']
            linkedin_link = form.cleaned_data['linkedin_link']
            profile_photo = form.cleaned_data['profile_photo']

            new_profile = Profile(profile_name=profile_name,
                                  first_name=first_name,
                                  last_name=last_name,
                                  about=about,
                                  github_link=github_link,
                                  twitter_link=twitter_link,
                                  linkedin_link=linkedin_link,
                                  profile_photo=profile_photo)

            new_profile.user_id = request.user
            new_profile.save()

            # Saving experiences
            for i in range(len(request.POST.getlist('company_name'))):
                company_name = request.POST.getlist('company_name')[i]
                job_profile = request.POST.getlist('job_profile')[i]
                exp_start_date = request.POST.getlist('exp_start_date')[i]
                exp_end_date = request.POST.getlist('exp_end_date')[i]
                details = request.POST.getlist('details')[i]

                new_experience = Experience(profile_id=new_profile,
                                            company_name=company_name,
                                            job_profile=job_profile,
                                            exp_start_date=exp_start_date,
                                            exp_end_date=exp_end_date,
                                            details=details)
                new_experience.save()

            # Saving projects
            for i in range(len(request.POST.getlist('project_name'))):
                project_name = request.POST.getlist('project_name')[i]
                proj_start_date = request.POST.getlist('proj_start_date')[i]
                proj_end_date = request.POST.getlist('proj_end_date')[i]
                project_details = request.POST.getlist('project_details')[i]
                project_code_link = request.POST.getlist(
                    'project_code_link')[i]
                project_link = request.POST.getlist('project_link')[i]
                print(request.FILES.getlist('project_photo'))
                if request.FILES.getlist('project_photo'):
                    project_photo = request.FILES.getlist('project_photo')[i]
                else:
                    project_photo = None

                new_project = Project(profile_id=new_profile,
                                      project_name=project_name,
                                      proj_start_date=proj_start_date,
                                      proj_end_date=proj_end_date,
                                      project_details=project_details,
                                      project_code_link=project_code_link,
                                      project_link=project_link,
                                      project_photo=project_photo)

                new_project.save()

            # Saving educations
            for i in range(len(request.POST.getlist('school'))):
                school = request.POST.getlist('school')[i]
                edu_end_date = request.POST.getlist('edu_end_date')[i]
                degree = request.POST.getlist('degree')[i]
                city = request.POST.getlist('city')[i]
                country = request.POST.getlist('country')[i]
                grade = request.POST.getlist('grade')[i]

                new_education = Education(
                    profile_id=new_profile,
                    school=school,
                    edu_end_date=edu_end_date,
                    degree=degree,
                    city=city,
                    country=country,
                    grade=grade
                )

                new_education.save()

            return redirect('index')

    form = CreateProfileForm()
    experience_form = CreateExperienceForm()
    project_form = CreateProjectForm()
    education_form = CreateEducationForm()
    getRequest = True
    context = {
        'form': form,
        'experience_form': experience_form,
        'project_form': project_form,
        'edu_form': education_form,
        'getRequest': getRequest
    }
    return render(request, 'foliomine/create_profile.html', context)


def displayProfile(request, profile_id):
    profile = Profile.objects.get(id=profile_id)
    experiences = Experience.objects.filter(profile_id=profile_id)
    projects = Project.objects.filter(profile_id=profile_id)
    educations = Education.objects.filter(profile_id=profile_id)

    edu_len = len(educations)
    proj_len = len(projects)
    exp_len = len(experiences)
    context = {
        'profile': profile,
        'experiences': experiences,
        'projects': projects,
        'proj_len': proj_len,
        'exp_len': exp_len,
        'educations': educations,
        'edu_len': edu_len
    }
    return render(request, 'foliomine/display_profile.html', context)


@login_required
def edit_profile(request, profile_id):

    profile = Profile.objects.get(id=profile_id)
    experiences = profile.experience_set.all()
    projects = profile.project_set.all()
    educations = profile.education_set.all()
    
    if request.method == 'POST':
        print(request.POST)
        # Updating profile
        profile.profile_name = request.POST.getlist('profile_name')[0]
        profile.first_name = request.POST.getlist('first_name')[0]
        profile.last_name = request.POST.getlist('last_name')[0]
        profile.about = request.POST.getlist('about')[0]
        profile.profile_photo = request.POST.getlist('profile_photo')[0]
        profile.github_link = request.POST.getlist('github_link')[0]
        profile.twitter_link = request.POST.getlist('twitter_link')[0]
        profile.linkedin_link = request.POST.getlist('linkedin_link')[0]
        profile.save()

        # Updating experience
        for i in range(len(request.POST.getlist('company_name'))):
            if i < len(experiences):
                experiences[i].exp_start_date = request.POST.getlist('exp_start_date')[i]
                experiences[i].exp_end_date = request.POST.getlist('exp_end_date')[i]
                experiences[i].job_profile = request.POST.getlist('job_profile')[i]
                experiences[i].company_name = request.POST.getlist('company_name')[i]
                experiences[i].details = request.POST.getlist('details')[i]
                experiences[i].save()
                continue

            new_experience = Experience(
                profile_id=profile,
                company_name=request.POST.getlist('company_name')[i],
                exp_start_date=request.POST.getlist('exp_start_date')[i],
                exp_end_date=request.POST.getlist('exp_end_date')[i],
                job_profile=request.POST.getlist('job_profile')[i],
                details=request.POST.getlist('details')[i]
            )
            new_experience.save()
        
        #Updating profile
        for i in range(len(request.POST.getlist('project_name'))):
            if i < len(projects):
                print(request.FILES.getlist('project_photo_'+str(i)))
                print(projects[i])
                projects[i].project_name = request.POST.getlist('project_name')[i]
                projects[i].proj_start_date = request.POST.getlist('proj_start_date')[i]
                projects[i].proj_end_date = request.POST.getlist('proj_end_date')[i]
                projects[i].project_details = request.POST.getlist('project_details')[i]
                projects[i].project_code_link = request.POST.getlist('project_code_link')[i]
                projects[i].project_link = request.POST.getlist('project_link')[i]
                if len(request.FILES.getlist('project_photo_'+str(i+1))) > 0:
                    projects[i].project_photo = request.FILES.getlist('project_photo_'+str(i+1))[0]
                    
                projects[i].save()
                continue
            
            if len(request.FILES.getlist('project_photo')) > 0:
                new_project = Project(
                    profile_id=profile,
                    project_name=request.POST.getlist('project_name')[i],
                    proj_start_date=request.POST.getlist('proj_start_date')[i],
                    proj_end_date=request.POST.getlist('proj_end_date')[i],
                    project_details=request.POST.getlist('project_details')[i],
                    project_code_link=request.POST.getlist('project_code_link')[i],
                    project_link=request.POST.getlist('project_link')[i],
                    project_photo=request.FILES.getlist('project_photo')[len(projects) - i]
                )
            else:
                new_project = Project(
                    profile_id=profile,
                    project_name=request.POST.getlist('project_name')[i],
                    proj_start_date=request.POST.getlist('proj_start_date')[i],
                    proj_end_date=request.POST.getlist('proj_end_date')[i],
                    project_details=request.POST.getlist('project_details')[i],
                    project_code_link=request.POST.getlist('project_code_link')[i],
                    project_link=request.POST.getlist('project_link')[i],
                )
            new_project.save()
        
        # Updating education
        for i in range(len(request.POST.getlist('school'))):
            if i < len(educations):
                educations[i].school = request.POST.getlist('school')[i]
                educations[i].edu_end_date = request.POST.getlist('edu_end_date')[i]
                educations[i].degree = request.POST.getlist('degree')[i]
                educations[i].city = request.POST.getlist('city')[i]
                educations[i].country = request.POST.getlist('country')[i]
                educations[i].grade = request.POST.getlist('grade')[i]

                educations[i].save()
                continue
            
            new_education = Education(
                profile_id=profile,
                edu_end_date=request.POST.getlist('edu_end_date')[i],
                degree=request.POST.getlist('degree')[i],
                city=request.POST.getlist('city')[i],
                country=request.POST.getlist('country')[i],
                grade=request.POST.getlist('grade')[i],
                school=request.POST.getlist('school')[i]
            )
            new_education.save()
            

    form = CreateProfileForm()
    experience_form = CreateExperienceForm()
    project_form = CreateProjectForm()
    education_form = CreateEducationForm() 
    exp_len_json = dumps(len(experiences))
    proj_len_json = dumps(len(projects))
    edu_len_json = dumps(len(educations))

    exp_dates = [
        {
            'exp_start_date': experience.exp_start_date,
            'exp_end_date': experience.exp_end_date
        }
        for experience in experiences
    ]
    proj_dates = [
        {
            'proj_start_date':project.proj_start_date,
            'proj_end_date': project.proj_end_date,
        }
        for project in projects
    ]

    edu_dates = [
        {
            'edu_end_date': education.edu_end_date
        }
        for education in educations
    ]

    exp_json = dumps(exp_dates, cls=CustomJSONEncoder)
    proj_json = dumps(proj_dates, cls=CustomJSONEncoder)
    edu_json = dumps(edu_dates, cls=CustomJSONEncoder)

    context = {
        'profile': profile,
        'profile_id': profile_id,
        'form': form,
        'experience_form': experience_form,
        'project_form': project_form,
        'edu_form': education_form,
        'experiences': experiences,
        'exp_len_json': exp_len_json,
        'exp_json': exp_json,
        'projects': projects,
        'proj_len_json': proj_len_json,
        'proj_json': proj_json,
        'educations': educations,
        'edu_len_json': edu_len_json,
        'edu_json': edu_json
    }

    return render(request, 'foliomine/edit_profile.html', context)


# To handle the serialization of date object from experience.
class CustomJSONEncoder(JSONEncoder):

    def default(self, obj):
        # Checks if obj is an instance of date, if it is, then return
        # isoformat of date so that it becomes serializable
        if isinstance(obj, date):
            return obj.isoformat()
        return super().default(obj)