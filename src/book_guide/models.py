from typing import ValuesView
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse, reverse_lazy

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
        return reverse('genre_data', args=[self.pk])        

    class Meta:
        verbose_name='Жанр'
        verbose_name_plural='Жанры'      

class Author(models.Model):
    name = models.CharField(
        verbose_name='Автор',
        max_length=50,
    )

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse('author_detail', args=[self.pk])


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
        return reverse('lines_data', args=[self.pk])

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
        return reverse('publisher_data', args=[self.pk])

    class Meta:
        verbose_name='Издатель'
        verbose_name_plural='Издатели' 

class Book(models.Model): 
    name = models.CharField(
        verbose_name='Название книги',
        max_length=40)
    # фото обложки
    price = models.FloatField(
        verbose_name='Цена (BYN)'
    ) 

    author = models.ForeignKey(
        Author, 
        on_delete=models.PROTECT,
        verbose_name='Автор'
    )

    line = models.ForeignKey(
        Line, 
        on_delete=models.PROTECT,
        verbose_name='Серия',
    )   
 

    genre = models.ForeignKey(
        Genre, 
        on_delete=models.PROTECT,
        verbose_name='Жанр'
    )
    

    publication_date = models.DateTimeField(
        verbose_name='Год издания',
        auto_now=False,	
        auto_now_add=True
    )

    pages = models.IntegerField(
        verbose_name='Количество страниц',
        default=0
    )
    #binding= переплет 
    #ISBN
    #вес (гр)
    age_restrictions = models.BooleanField(
        verbose_name='возрастные ограничения',
        default=False
    )
    
    publisher = models.ForeignKey(
        Publisher, 
        on_delete=models.PROTECT,
        verbose_name='Издатель',
    )     

    quantity_on_hand = models.IntegerField(
        verbose_name='количество книг в наличии'
        #number=models.models.ForeignKey()
    )
    active = models.BooleanField(
        verbose_name='доступен для заказа, ДА/Нет',
        default=False
    )
    rating = models.IntegerField(
        verbose_name='рейтинг (0 - 10)',
        default=0
    )
        
     #created = models.DateTimeField(
    #    verbose_name='дата внесения в каталог',
    #    auto_now=False,	
    #    auto_now_add=True
    #)
    #updated = models.DateTimeField(
    #    verbose_name='дата последнего редактирования карточки',
    #    auto_now_add=True,
    #    auto_created=False
    #)
    def __str__(self) -> str:
        return f'Книга: {self.name}'

    class Meta:
        verbose_name='Книгу'
        verbose_name_plural='Книги'

