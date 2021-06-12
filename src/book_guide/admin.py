from django.contrib import admin
from django.db.models.base import Model

# Register your models here.
from . import models



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



