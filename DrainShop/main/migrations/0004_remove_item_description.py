# Generated by Django 4.2.5 on 2024-04-22 11:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_item_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='description',
        ),
    ]
