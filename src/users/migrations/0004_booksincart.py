# Generated by Django 3.2.3 on 2021-06-24 10:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_alter_book_name'),
        ('users', '0003_auto_20210624_0008'),
    ]

    operations = [
        migrations.CreateModel(
            name='BooksInCart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1, verbose_name='Quantity')),
                ('unit_price', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Unit_price')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='books.book', verbose_name='Book')),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.cart', verbose_name='Cart')),
            ],
        ),
    ]
