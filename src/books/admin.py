from django.contrib import admin

from django.db.models.base import Model
from . import models


class BookAdmin(admin.ModelAdmin):
    list_display = [
        'pk',
        'name',
        'author',
        'line',
        'genre',
        'price',
        'publication_date',
        'pages',
        'publisher',
        'age_restrictions',
        'quantity_on_hand',
        'active',
        'rating',
    ]


admin.site.register(models.Book, BookAdmin)