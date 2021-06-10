# Generated by Django 3.2.3 on 2021-06-10 12:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('book_guide', '0018_book_picture'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='Название книги')),
                ('price', models.FloatField(verbose_name='Цена (BYN)')),
                ('publication_date', models.DateTimeField(auto_now_add=True, verbose_name='Год издания')),
                ('pages', models.IntegerField(default=0, verbose_name='Количество страниц')),
                ('picture', models.ImageField(upload_to='books/%Y/%m/%d/', verbose_name='Картинка')),
                ('age_restrictions', models.BooleanField(default=False, verbose_name='возрастные ограничения')),
                ('quantity_on_hand', models.IntegerField(verbose_name='количество книг в наличии')),
                ('active', models.BooleanField(default=False, verbose_name='доступен для заказа, ДА/Нет')),
                ('rating', models.IntegerField(default=0, verbose_name='рейтинг (0 - 10)')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='autors', to='book_guide.author', verbose_name='Автор')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='genres', to='book_guide.genre', verbose_name='Жанр')),
                ('line', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='lines', to='book_guide.line', verbose_name='Серия')),
                ('publisher', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='genres', to='book_guide.publisher', verbose_name='Издатель')),
            ],
            options={
                'verbose_name': 'Книгу',
                'verbose_name_plural': 'Книги',
            },
        ),
    ]
