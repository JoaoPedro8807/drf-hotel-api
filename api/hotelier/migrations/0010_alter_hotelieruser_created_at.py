# Generated by Django 5.0.6 on 2024-06-26 13:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotelier', '0009_alter_hotelieruser_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotelieruser',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime.now, editable=False),
        ),
    ]
