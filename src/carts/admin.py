from django.contrib import admin
from . import models

# Register your models here.

class CartAdmin(admin.ModelAdmin):
    list_display = [
        'pk',
        'customer',
        'order_date',
        'total_price',
    ]

class BooksInCartAdmin(admin.ModelAdmin):
    list_display = [
        'pk',
        'cart',
        'quantity',
        'unit_price'
    ]    

admin.site.register(models.Cart, CartAdmin)   
admin.site.register(models.BooksInCart, BooksInCartAdmin)  