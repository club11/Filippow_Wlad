from django.contrib import admin
from . import models

# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    list_display = [
        'pk',
        'user',
        'tel',
        'first_name',
        'last_name',
        'email',
        'group',
        'home_adress',
        'country',
        'city',
        'home_index',
        # need extention with  country city index adress1 adress2
        'another_info',  
    ]  


admin.site.register(models.Profile, ProfileAdmin)



