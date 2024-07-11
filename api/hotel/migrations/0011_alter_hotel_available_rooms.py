# Generated by Django 5.0.6 on 2024-06-27 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0010_alter_hotel_created_at_alter_hotel_updated_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='available_rooms',
            field=models.IntegerField(default=0, verbose_name='number of available rooms'),
        ),
    ]