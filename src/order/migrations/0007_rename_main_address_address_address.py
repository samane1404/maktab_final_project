# Generated by Django 4.0.1 on 2022-02-02 10:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0006_alter_orderitem_user_address_order_address'),
    ]

    operations = [
        migrations.RenameField(
            model_name='address',
            old_name='main_address',
            new_name='address',
        ),
    ]