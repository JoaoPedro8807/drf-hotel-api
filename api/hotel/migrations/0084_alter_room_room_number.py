# Generated by Django 5.0.6 on 2024-07-07 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0083_alter_room_room_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='room_number',
            field=models.PositiveIntegerField(verbose_name='room number'),
        ),
    ]
