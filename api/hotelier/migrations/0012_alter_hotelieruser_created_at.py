# Generated by Django 5.0.6 on 2024-06-26 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotelier', '0011_remove_hotelieruser_birthday'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotelieruser',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
