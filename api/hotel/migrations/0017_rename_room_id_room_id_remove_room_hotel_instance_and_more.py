# Generated by Django 5.0.6 on 2024-06-28 18:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0016_rename_hotel_id_hotel_id_remove_room_hotel_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='room',
            old_name='room_id',
            new_name='id',
        ),
        migrations.RemoveField(
            model_name='room',
            name='hotel_instance',
        ),
        migrations.AddField(
            model_name='room',
            name='hotel',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='room', to='hotel.hotel', verbose_name='hotel'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='room',
            name='room_type',
            field=models.CharField(choices=[('T', 'TRIPLE'), ('S', 'SINGLE'), ('D', 'DOUBLE')], max_length=2, verbose_name='room type'),
        ),
    ]
