# Generated by Django 5.0.6 on 2024-06-28 18:07

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0015_remove_hotel_id_remove_hotel_uuid_remove_room_uuid_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hotel',
            old_name='hotel_id',
            new_name='id',
        ),
        migrations.RemoveField(
            model_name='room',
            name='hotel',
        ),
        migrations.RemoveField(
            model_name='room',
            name='id',
        ),
        migrations.AddField(
            model_name='room',
            name='hotel_instance',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='room_alterar', to='hotel.hotel', verbose_name='hotel'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='room',
            name='room_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='room',
            name='room_type',
            field=models.CharField(choices=[('D', 'DOUBLE'), ('S', 'SINGLE'), ('T', 'TRIPLE')], max_length=2, verbose_name='room type'),
        ),
    ]
