# Generated by Django 4.0.1 on 2022-01-31 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='ordered',
            field=models.BooleanField(default=False),
        ),
    ]
