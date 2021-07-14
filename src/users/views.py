from django import template
from django.contrib.auth import authenticate, get_user_model, login, models, password_validation
from django.db.models.fields import related
from django.forms import forms

from django.contrib.auth import forms
from django.shortcuts import redirect
from django.contrib.auth.views import LoginView, PasswordChangeView, PasswordChangeDoneView

from django.contrib.auth.models import User
#from .models import UserProfile
#from .forms import UserProfileForm
from django.views.generic import  FormView, DetailView, UpdateView, View
from django.http import HttpResponse, HttpResponseRedirect

from . import models, forms
from django.urls import reverse_lazy

from carts import models as carts_models

User = get_user_model()

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

class ProfileView(UpdateView):
    model = models.Profile
    #form_class = forms.RegisterForm
    template_name = 'users/profile_change.html'
    fields = (                                      #для UpdateView, не забыть заменить при DetailView
        'tel',
        'first_name',
        'last_name',
        'email',
        'group',
        'another_info',
        'country',
        'city',
        'home_adress',
        'home_index',
        )
    success_url = reverse_lazy('login:profile_change')

    def get_object(self, queryset=None):
        user_profile=models.Profile.objects.get(user=self.request.user)
        return user_profile

class CustomerProfileView(UpdateView):
    model = models.Profile
    template_name = 'users/customer_profile_change.html'
    fields = (                                      
        'group',
        'another_info',
        'country',
        'city',
        'home_adress',
        'home_index',
        )
    success_url = reverse_lazy('orders:order_list')             ###ЗАГЛУШКА / НЕ ОБНОВЛЯЕТ ПО PK

    def get_object(self, queryset=None):
            if queryset is None:
                queryset = self.get_queryset()
            pk = self.kwargs.get(self.pk_url_kwarg)
            slug = self.kwargs.get(self.slug_url_kwarg)
            if pk is not None:
                queryset = queryset.filter(pk=pk)
            if slug is not None and (pk is None or self.query_pk_and_slug):
                slug_field = self.get_slug_field()
                queryset = queryset.filter(**{slug_field: slug})
            obj = queryset.get()
            if pk is None and slug is None:
                raise AttributeError(
            "Generic detail view %s must be called with either an object "
            "pk or a slug in the URLconf." % self.__class__.__name__
            )
            try:
                obj = queryset.get()
            except queryset.model.DoesNotExist:
                raise Http404(_("No %(verbose_name)s found matching the query") %
                      {'verbose_name': queryset.model._meta.verbose_name})
            print(obj)
            print(obj.pk)           
            return obj

        #    user_profile = models.Profile.objects.get(pk=int(object_id))
        #    return user_profile

class AdminPortalView(FormView):
    form_class = forms.AdminPortalForm
    template_name = 'users/admin_portal.html'