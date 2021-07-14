#from project_shop.src import comments
from django.db import models


from django.contrib.contenttypes.fields import GenericRelation
from comments.models import Comment
from carts import models as carts_models
from django.urls import reverse, reverse_lazy
# Create your models here.

class Order(models.Model):
    cart = models.ForeignKey(
        carts_models.Cart,
        on_delete=models.PROTECT,
        verbose_name='Order',
        related_name='orders',
    )

    order_status= models.ForeignKey(
        'OrderStatus', 
        on_delete=models.PROTECT,
        verbose_name='Статус',
        related_name='status',
        default=1
    )                                        ##### статус заказа 02:02:44

    contact_info = models.TextField(                ### 02:02:00
        verbose_name='Contact_info',
    )   
    created = models.DateTimeField(
        verbose_name='created',
        auto_now=False,
        auto_now_add=True
    )
    updated = models.DateTimeField(
        verbose_name='updated',
        auto_now=True,
        auto_now_add=False
    )

    comments = GenericRelation(Comment)

class OrderStatus(models.Model):
    name = models.CharField(
        verbose_name='Статус заказа',
        max_length=20,
        blank=True
    )

    def __str__(self):
        return self.name

    #def get_absolute_url(self):
    #    return reverse('book_guide:lines_data', args=[self.pk])    