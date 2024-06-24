# Generated by Django 5.0.6 on 2024-06-09 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_order_default_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='default_price',
        ),
        migrations.AddField(
            model_name='item',
            name='default_price',
            field=models.IntegerField(default=1999),
        ),
    ]
