from django.db import models

#from django.contrib.auth.models import User   #my old version
from django.contrib.auth import get_user_model #the new_one

User = get_user_model()     # in order to get an active User model

class Profile(models.Model):
    user = models.OneToOneField(
        User,
        verbose_name="User account",
        on_delete=models.CASCADE,
        related_name='profile'              #how  model User may asks user(Profile)
    )
    tel = models.CharField(
        verbose_name="Tel number",
        max_length=15      
    )
    first_name = models.CharField('first name', max_length=150, blank=True,)
    last_name = models.CharField('last name', max_length=150, blank=True,)
    email = models.EmailField('email address', blank=True,) 
    group = models.CharField(verbose_name="Группа", max_length=25, default='none')
    home_adress = models.CharField(verbose_name="Домашний дрес", max_length=50, blank=True)
# need extention with  country city index adress1 adress2
    another_info = models.CharField(verbose_name="Дополнительная информация", max_length=100, blank=True)

    country = models.CharField(max_length=20, verbose_name='страна')
    city = models.CharField(max_length=20, verbose_name='город')
    home_index = models.IntegerField(verbose_name='индекс')
    
