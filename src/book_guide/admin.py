from django.contrib import admin

# Register your models here.
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

class GenreAdmin(admin.ModelAdmin):
    list_display = [
        'pk',
        'name',
        'description'
    ]

class AuthorAdmin(admin.ModelAdmin):
    list_display = [
        'pk',
        'name'
    ]

class LineAdmin(admin.ModelAdmin):
    list_display = [
        'pk',
        'name'
    ]

class PublisherAdmin(admin.ModelAdmin):
    list_display = [
        'pk',
        'name'
    ]

admin.site.register(models.Genre, GenreAdmin)
admin.site.register(models.Author, AuthorAdmin)
admin.site.register(models.Line, LineAdmin)
admin.site.register(models.Publisher, PublisherAdmin)
admin.site.register(models.Book, BookAdmin)


