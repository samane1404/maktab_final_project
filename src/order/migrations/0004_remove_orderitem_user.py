# Generated by Django 4.0.1 on 2022-01-31 22:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_orderitem_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='user',
        ),
    ]
