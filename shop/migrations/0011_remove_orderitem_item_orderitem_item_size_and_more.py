# Generated by Django 5.0.6 on 2024-06-09 05:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_order_address_order_total_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='item',
        ),
        migrations.AddField(
            model_name='orderitem',
            name='item_size',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='shop.itemsize'),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('CREATED_ORDER', 'Заказ создан'), ('ACCEPTED_ORDER', 'Заказ принят'), ('DELIVERED_ORDER', 'Заказ доставлен'), ('COMPLETED_ORDER', 'Заказ завершен'), ('CANCELLED_ORDER', 'Заказ отменен')], default=('CREATED_ORDER', 'Заказ создан'), max_length=128),
        ),
    ]