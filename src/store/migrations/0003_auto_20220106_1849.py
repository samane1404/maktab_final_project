# Generated by Django 3.2.2 on 2022-01-06 15:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_auto_20220106_1644'),
    ]

    operations = [
        migrations.RenameField(
            model_name='branch',
            old_name='category_food_id',
            new_name='category_food',
        ),
        migrations.RenameField(
            model_name='branch',
            old_name='manager_id',
            new_name='manager',
        ),
        migrations.RenameField(
            model_name='branch',
            old_name='restaurant_id',
            new_name='restaurant',
        ),
        migrations.RenameField(
            model_name='food',
            old_name='category_food_id',
            new_name='category_food',
        ),
        migrations.RenameField(
            model_name='food',
            old_name='category_meel_id',
            new_name='category_meel',
        ),
        migrations.RenameField(
            model_name='menu',
            old_name='branch_id',
            new_name='branch',
        ),
        migrations.RenameField(
            model_name='menu',
            old_name='food_id',
            new_name='food',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='customer_id',
            new_name='customer',
        ),
        migrations.RenameField(
            model_name='orderitem',
            old_name='menu_id',
            new_name='menu',
        ),
        migrations.RenameField(
            model_name='orderitem',
            old_name='order_id',
            new_name='order',
        ),
    ]
