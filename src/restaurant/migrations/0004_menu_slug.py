# Generated by Django 4.0.1 on 2022-01-31 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0003_alter_menu_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]