from django.db import models

from carts import models as carts_models

# Create your models here.

class Order(models.Model):
    cart = models.ForeignKey(
        carts_models.Cart,
        on_delete=models.PROTECT,
        verbose_name='Order'
    )

    #status                                         ##### статус заказа 02:02:44

    contact_info = models.TextField(                ### 02:02:00
        verbose_name='Contact_info',
    )  

    #tel = models.TextField(                
    #    verbose_name='Tel',
    #)  

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