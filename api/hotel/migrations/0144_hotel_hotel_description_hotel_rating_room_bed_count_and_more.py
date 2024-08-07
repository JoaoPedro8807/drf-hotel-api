# Generated by Django 5.0.6 on 2024-07-16 18:19

import hotel.models.room_model
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0143_alter_room_room_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='hotel_description',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='hotel',
            name='rating',
            field=models.FloatField(default=1, verbose_name='number of rating'),
        ),
        migrations.AddField(
            model_name='room',
            name='bed_count',
            field=models.PositiveIntegerField(blank=True, default=1, verbose_name='number of bed in room'),
        ),
        migrations.AddField(
            model_name='room',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=hotel.models.room_model.room_image_upload_path),
        ),
        migrations.AddField(
            model_name='room',
            name='room_description',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='available_rooms',
            field=models.PositiveIntegerField(default=0, verbose_name='number of available rooms'),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='total_rooms',
            field=models.PositiveIntegerField(blank=True, verbose_name='numbers of rooms'),
        ),
        migrations.AlterField(
            model_name='room',
            name='room_type',
            field=models.CharField(choices=[('S', 'SINGLE'), ('T', 'TRIPLE'), ('D', 'DOUBLE')], max_length=1, verbose_name='room type'),
        ),
    ]
