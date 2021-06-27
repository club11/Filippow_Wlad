from typing import ValuesView
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse, reverse_lazy

#from book_guide.models import Genre, Author, Line, Publisher
#import book_guide.models
#from .models import Genre, Author, Line, Publisher

from book_guide.models import Genre, Author, Line, Publisher

class Book(models.Model): 
    name = models.CharField(
        verbose_name='Название книги',
        max_length=60)
    # фото обложки
    price = models.FloatField(
        verbose_name='Цена (BYN)'
    ) 

    author = models.ForeignKey(
        Author, 
        on_delete=models.PROTECT,
        verbose_name='Автор',
        related_name='autors',
    )

    line = models.ForeignKey(
        Line, 
        on_delete=models.PROTECT,
        verbose_name='Серия',
        related_name='lines',
    )   
 

    genre = models.ForeignKey(
        Genre, 
        on_delete=models.PROTECT,
        verbose_name='Жанр',
        related_name='genres',
    )

    publisher = models.ForeignKey(
        Publisher, 
        on_delete=models.PROTECT,
        verbose_name='Издатель',
        related_name='genres',
    )        

    publication_date = models.DateTimeField(
        verbose_name='Год издания',
        auto_now=False,	
        auto_now_add=True,
    )

    pages = models.IntegerField(
        verbose_name='Количество страниц',
        default=0
    )
    #binding= переплет 
    picture = models.ImageField(
        "Картинка",
        upload_to='books/%Y/%m/%d/'
    )
    #ISBN
    #вес (гр)
    age_restrictions = models.BooleanField(
        verbose_name='возрастные ограничения',
        default=False
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
        return f'{self.name}'


    def get_absolute_url(self):
        return reverse('books_list:book_detail', args=[self.pk])      

    class Meta:
        verbose_name='Книгу'
        verbose_name_plural='Книги'
