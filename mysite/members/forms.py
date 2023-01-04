from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class RegisterUserForm(UserCreationForm):

    email = forms.EmailField(max_length=50, widget=forms.EmailInput(attrs={'class':'text-white-200'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        labels = ('Username:', 'Email:', 'Password:', 'Confirm password:')
