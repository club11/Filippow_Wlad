# Generated by Django 3.2.3 on 2021-05-23 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='название жанра')),
                ('description', models.CharField(max_length=40, verbose_name='описание жанра')),
            ],
        ),
    ]
