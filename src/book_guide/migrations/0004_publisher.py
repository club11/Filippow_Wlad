# Generated by Django 3.2.3 on 2021-05-23 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_guide', '0003_line'),
    ]

    operations = [
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Издатель')),
            ],
        ),
    ]
