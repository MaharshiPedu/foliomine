from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import CreateProfileForm
from .models import Profile


def index(request):
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
            
            new_profile = Profile(profile_name=profile_name, first_name=first_name, last_name=last_name, about=about,
                                  github_link=github_link, twitter_link=twitter_link, linkedin_link=linkedin_link, profile_photo=profile_photo)
            new_profile.user_id = request.user
            new_profile.save()

            return redirect('index')

    form = CreateProfileForm()
    return render(request, 'foliomine/create_profile.html', {'form': form})
