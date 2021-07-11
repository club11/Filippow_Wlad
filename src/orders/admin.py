from django.contrib import admin
from . import models

# Register your models here.

class OrderAdmin(admin.ModelAdmin):
    list_display = [
        'pk',
        'order_status',
        #'tel'
        'contact_info',
        'created',
        'updated',
    ]  


class OrderStatusAdmin(admin.ModelAdmin):
    list_display = [
        'pk',
        'name'
    ]    

    
admin.site.register(models.Order, OrderAdmin)  
admin.site.register(models.OrderStatus, OrderStatusAdmin)
