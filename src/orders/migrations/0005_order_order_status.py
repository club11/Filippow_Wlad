# Generated by Django 3.2.3 on 2021-07-11 11:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_orderstatus'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order_status',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='status', to='orders.orderstatus', verbose_name='Статус'),
            preserve_default=False,
        ),
    ]
