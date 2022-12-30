from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CreateProfileForm


def index(request):
    return render(request, 'foliomine/index.html', {})


def create_profile(request):
    # if request.method == 'POST':
    #     form = CreateProfileForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         first_name = form.cleaned_data['first_name']
    #         last_name = form.cleaned_data['last_name']
    #         about = form.cleaned_data['about']
    #         last_name = form.cleaned_data['last_name']
    #         last_name = form.cleaned_data['last_name']
            
    #         return redirect('index')

    form = CreateProfileForm()
    return render(request, 'foliomine/create_profile.html', {'form':form})
