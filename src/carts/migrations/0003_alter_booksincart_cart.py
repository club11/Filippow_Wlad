# Generated by Django 3.2.3 on 2021-06-27 10:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0002_cart_order_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booksincart',
            name='cart',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='goods', to='carts.cart', verbose_name='Cart'),
        ),
    ]
