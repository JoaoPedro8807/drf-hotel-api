# Generated by Django 5.0.6 on 2024-06-26 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0009_alter_hotel_created_at_alter_room_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='created_at',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='updated_at',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='room',
            name='created_at',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='room',
            name='updated_at',
            field=models.DateField(auto_now=True),
        ),
    ]