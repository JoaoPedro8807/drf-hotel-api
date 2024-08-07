# Generated by Django 5.0.6 on 2024-06-26 13:49

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0005_hotel_created_at_room_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
        migrations.AlterField(
            model_name='room',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
    ]
