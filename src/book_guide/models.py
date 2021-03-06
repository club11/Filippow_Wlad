from typing import ValuesView
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse, reverse_lazy

from django.contrib.contenttypes.fields import GenericRelation
from comments.models import Comment

# Create your models here.

class Genre(models.Model):
    name = models.CharField(
        verbose_name='название жанра',
        max_length=20)
    description = models.CharField(
        verbose_name='описание жанра',
        max_length=40)  

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse('book_guide:genre_data', args=[self.pk])        

    class Meta:
        verbose_name='Жанр'
        verbose_name_plural='Жанры'      

class Author(models.Model):
    name = models.CharField(
        verbose_name='Автор',
        max_length=50,
    )

    comments = GenericRelation(Comment)

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse('book_guide:author_detail', args=[self.pk])


    class Meta:
        verbose_name='Автор'
        verbose_name_plural='Авторы'     

class Line(models.Model):
    name = models.CharField(
        verbose_name='Серия',
        max_length=50,
        blank=True
    )

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse('book_guide:lines_data', args=[self.pk])

    class Meta:
        verbose_name='Серия'
        verbose_name_plural='Серии'  


class Publisher(models.Model):
    name = models.CharField(
        verbose_name='Издатель',
        max_length=30
    )

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse('book_guide:publisher_data', args=[self.pk])

    class Meta:
        verbose_name='Издатель'
        verbose_name_plural='Издатели' 



