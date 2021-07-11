from django.contrib.auth import authenticate, get_user_model, login, models, password_validation
from django.db.models.fields import related
from django.forms import forms

from django.contrib.auth import forms
from django.shortcuts import redirect
from django.contrib.auth.views import LoginView, PasswordChangeView, PasswordChangeDoneView

from django.contrib.auth.models import User
#from .models import UserProfile
#from .forms import UserProfileForm
from django.views.generic import  FormView, DetailView, UpdateView
from django.http import HttpResponse, HttpResponseRedirect

from . import models, forms
from django.urls import reverse_lazy

User = get_user_model()


#class MyLoginPasswordChangeView(PasswordChangeView):
#   template_name = 'users/psd_change.html'
#   form_class = forms.PasswordChangeForm
#   success_url = reverse_lazy('login:login')


class Registerview(FormView):
    template_name = 'registration/register.html'
    form_class = forms.RegisterForm
    success_url = reverse_lazy('books_list:book_list')
    

    def form_valid(self, form):             # 1 раскидываем данные по моделям
        #1 зарегать сперва в стандартной джанговской модели
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        tel = form.cleaned_data.get('tel')

        home_index = form.cleaned_data.get('home_index')
        email = form.cleaned_data.get('email')
        first_name = form.cleaned_data.get('first_name')
        lastname = form.cleaned_data.get('lastname')
        country = form.cleaned_data.get('country')
        city = form.cleaned_data.get('city')
        home_adress = form.cleaned_data.get('home_adress')
        another_info = form.cleaned_data.get('another_info')

        #2 данные для готового пользователя
        user = User.objects.create_user(username=username, password=password)         #зарегать сперва в стандартной джанговской модели     
        # 2 досоздаем профиль под готового пользователя
        profile = models.Profile.objects.create(user=user, tel=tel, home_index=home_index, email=email, first_name=first_name, last_name=lastname, country=country, city=city, home_adress=home_adress, another_info=another_info)       # 2 досоздаем профиль под готового пользователя
        # 3 логиним пользователя
        login(self.request, user)
        return super().form_valid(form)



#class ProfileView(DetailView):
#    model = models.Profile
#    template_name = 'users/userprofile.html'
#    def get_object(self, queryset=None):
#        user_name = self.request.user.username
#        user_idd = self.request.user.pk
#        user_profile = models.Profile.objects.get(user_id=user_idd) # Здесь работает связь из user модели в кастомную profile (user id = 23 в user_profile_id = 11)
#        print(user_name)
#        print(user_idd)
#        print(user_profile)
#        print(user_profile.pk)
#        print(user_profile.email)
#        return user_profile



class ProfileView(UpdateView):
    model = models.Profile
    form_class = forms.RegisterUpdateForm
    template_name = 'users/profile_change.html'
    success_url = reverse_lazy('users:profile_change')

    def get_object(self, queryset=None):
        user_profile=models.Profile.objects.get(user=self.request.user)
        return user_profile

    #def get_object(self, queryset=None):
    #    return self.request.user.username 

    def form_valid(self, form):
        pk = self.request.user.pk
        user = User.objects.get(pk=pk)
        print(user)
        user = form.cleaned_data.get('user')
        first_name = form.cleaned_data.get('first_name')
        last_name = form.cleaned_data.get('last_name')
        tel = form.cleaned_data.get('tel')
        email = form.cleaned_data.get('email')
        another_info = form.cleaned_data.get('another_info')
        country = form.cleaned_data.get('country')
        city = form.cleaned_data.get('city')
        home_adress = form.cleaned_data.get('home_adress')
        home_index = form.cleaned_data.get('home_index')
        profile = models.Profile.objects.filter(user=user).update(
            user = user,
            first_name = first_name,
            last_name = last_name,
            tel = email,
            email= email, 
            another_info = another_info,
            country = country, 
            city = city, 
            home_adress = home_adress,
            home_index= home_index,
        )
        return HttpResponseRedirect(self.get_success_url())






#class ProfileView(UpdateView):
#    model = models.Profile
#    form_class = forms.RegisterForm
#    template_name = 'users/profile_change.html'
#    fields = (                                      #для UpdateView, не забыть заменить при DetailView
#        'tel',
#        'first_name',
#        'last_name',
#        'email',
#        'group',
#        'another_info',
#        'country',
#        'city',
#        'home_adress',
#        'home_index',
#        )
#    success_url = reverse_lazy('login:profile_change')

#    def get_object(self, queryset=None):
#        user_profile=models.Profile.objects.get(user=self.request.user)
#        return user_profile

    #def form_valid(self, form):
    #    form = forms.RegisterForm
    #    print('23')
    #    pk = self.request.user.pk
    #    print(pk)
    #    user = User.objects.get(pk=pk)
    #    print(user)
    #    first_name = form.cleaned_data.get('first_name')
    #    print(first_name)
    #
    #    return HttpResponseRedirect(self.get_success_url())

