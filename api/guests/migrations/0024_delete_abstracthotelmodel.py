# Generated by Django 5.0.6 on 2024-06-27 18:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('guests', '0023_abstracthotelmodel'),
        ('hotelier', '0018_remove_hotelieruser_abstracthotelmodel_ptr_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='AbstractHotelModel',
        ),
    ]
