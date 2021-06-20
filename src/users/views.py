from django.forms import forms
from django.shortcuts import render

from django.contrib.auth import forms
from django.shortcuts import redirect
from django.contrib.auth.views import LoginView, PasswordChangeView, PasswordChangeDoneView

from django.contrib.auth.models import User
from .models import UserProfile
from .forms import UserProfileForm
from django.views.generic import CreateView, DetailView

class MyLoginView(LoginView):
    template_name = 'users/userlogin.html'


class MyLoginPasswordChangeView(PasswordChangeView):
    template_name = 'users/passwordchange.html'
    form_class = forms.PasswordChangeForm




#class UserProfileDetailView(DetailView):
#    form_class = UserProfileForm
#    template_name = 'users/userprofile.html'
#    model = UserProfile

