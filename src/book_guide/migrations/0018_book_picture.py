# Generated by Django 3.2.3 on 2021-06-08 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_guide', '0017_auto_20210523_1924'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='picture',
            field=models.ImageField(default='ddstrokanakartinku', upload_to='books/%Y/%m/%d/', verbose_name='Картинка'),
            preserve_default=False,
        ),
    ]
