from django import forms
from django.forms import fields 
from . import models

class CreatePublisherForm(forms.ModelForm):
    class Meta:
        model = models.Publisher
        fields = ('name',)

class CreateAuthorForm(forms.ModelForm):
    class Meta:
        model = models.Author
        fields = ('name',)

class CreateLineForm(forms.ModelForm):
    class Meta:
        model = models.Line
        fields = ('name',)

class CreateGenreForm(forms.ModelForm):
    class Meta:
        model = models.Genre
        fields =[
            'name',
            'description',
        ]
