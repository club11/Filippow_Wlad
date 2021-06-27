from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
User = get_user_model()

from books import models as books_models

class Cart(models.Model):
    customer = models.ForeignKey(
        User, 
        null=True,
        blank=True,
        related_name='carts',
        verbose_name='Cart',
        on_delete=models.PROTECT
    )
    order_date = models.DateTimeField(
        verbose_name='Дата заказа',
        auto_now=False,	
        auto_now_add=True,
    )

    @property
    def total_price(self):
        total_price = 0
        goods = self.goods.all()
        for good in goods:
            total_price += good.total_price
        return total_price



class BooksInCart(models.Model):
    cart = models.ForeignKey(
        Cart,
        related_name='goods',
        on_delete=models.CASCADE,
        verbose_name='Cart'   
    )
    book = models.ForeignKey(
        'books.Book',
        on_delete=models.PROTECT,
        verbose_name='Book'
    )
    quantity = models.IntegerField(
        verbose_name='Quantity',
        default=1
    )
    unit_price = models.DecimalField(
        verbose_name='Unit_price',
        max_digits=5,
        decimal_places=2
    )

    @property
    def total_price(self):
        return self.unit_price * self.quantity