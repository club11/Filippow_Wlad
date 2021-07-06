from django.contrib.auth import get_user_model, login, models, password_validation
from django.db.models.fields import related
from django.forms import forms

from django.contrib.auth import forms
from django.shortcuts import redirect
from django.contrib.auth.views import LoginView, PasswordChangeView, PasswordChangeDoneView

from django.contrib.auth.models import User
#from .models import UserProfile
#from .forms import UserProfileForm
from django.views.generic import CreateView, DetailView, FormView
from . import models, forms
from django.urls import reverse_lazy

User = get_user_model()

#class MyLoginView(LoginView):
#    template_name = 'users/login.html'
    #redirect_field_name:
    #authentication_form:
    #redirect_authenticated_user: 


#class MyLoginPasswordChangeView(PasswordChangeView):
#    template_name = 'users/passwordchange.html'
#    form_class = forms.PasswordChangeForm


class Registerview(FormView):
    template_name = 'registration/register.html'
    form_class = forms.RegisterForm
    success_url = reverse_lazy('books_list:book_list')
    

    def form_valid(self, form):             # 1 раскидываем данные по моделям
        #1 зарегать сперва в стандартной джанговской модели
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        tel = form.cleaned_data.get('tel') 
        #2 данные для готового пользователя
        user = User.objects.create_user(username=username, password=password)         #зарегать сперва в стандартной джанговской модели     
        # 2 досоздаем профиль под готового пользователя
        profile = models.Profile.objects.create(user=user, tel=tel)                   # 2 досоздаем профиль под готового пользователя
        # 3 логиним пользователя
        login(self.request, user)
        return super().form_valid(form)












