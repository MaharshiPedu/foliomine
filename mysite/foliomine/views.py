from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.forms import formset_factory
from .forms import CreateProfileForm, CreateExperienceForm, CreateProjectForm
from .models import Profile, Experience, Project


def index(request):
    if request.user.is_authenticated:
        user = request.user
        profiles = Profile.objects.filter(user_id=user.id)
        return render(request, 'foliomine/index.html', {'profiles': profiles})

    return render(request, 'foliomine/index.html', {})


@login_required
def create_profile(request):
    print(request.POST)
    # experience_formset = formset_factory(CreateExperienceForm, extra=1)
    # project_formset = formset_factory(CreateProjectForm, extra=1)
    # project_forms = project_formset(request.POST, request.FILES)
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
                project_photo = request.FILES.getlist('project_photo')[i]

                new_project = Project(profile_id=new_profile,
                                      project_name=project_name,
                                      proj_start_date=proj_start_date,
                                      proj_end_date=proj_end_date,
                                      project_details=project_details,
                                      project_code_link=project_code_link,
                                      project_link=project_link,
                                      project_photo=project_photo)

                new_project.save()

            return redirect('index')

    form = CreateProfileForm()
    experience_form = CreateExperienceForm()
    project_form = CreateProjectForm()
    getRequest = True
    context = {
        'form': form,
        'experience_form': experience_form,
        'project_form': project_form,
        'getRequest': getRequest
    }
    return render(request, 'foliomine/create_profile.html', context)


def displayProfile(request, profile_id):
    profile = Profile.objects.get(id=profile_id)
    experiences = Experience.objects.filter(profile_id=profile_id)
    projects = Project.objects.filter(profile_id=profile_id)

    proj_len = len(projects)
    exp_len = len(experiences)
    context = {
        'profile': profile,
        'experiences': experiences,
        'projects': projects,
        'proj_len': proj_len,
        'exp_len': exp_len
    }
    return render(request, 'foliomine/display_profile.html', context)
