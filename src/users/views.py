from django.contrib.auth import get_user_model, models
from django.db.models.fields import related
from django.forms import forms

from django.contrib.auth import forms
from django.shortcuts import redirect
from django.contrib.auth.views import LoginView, PasswordChangeView, PasswordChangeDoneView

from django.contrib.auth.models import User
#from .models import UserProfile
#from .forms import UserProfileForm
from django.views.generic import CreateView, DetailView
from . import models

class MyLoginView(LoginView):
    template_name = 'users/userlogin.html'


class MyLoginPasswordChangeView(PasswordChangeView):
    template_name = 'users/passwordchange.html'
    form_class = forms.PasswordChangeForm



#class EmployeeCreateView(CreateView):
#    model = models.Employee
#    form_class = forms.CreateEmployeeForm








