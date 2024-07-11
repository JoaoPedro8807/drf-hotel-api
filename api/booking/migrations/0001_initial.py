# Generated by Django 5.0.6 on 2024-07-02 14:13

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('guests', '0024_delete_abstracthotelmodel'),
        ('hotel', '0023_alter_room_room_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('start_date', models.DateField(auto_now_add=True)),
                ('end_date', models.DateField(auto_now=True)),
                ('status', models.BooleanField(default=True, verbose_name='status')),
                ('guest', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='booking', to='guests.userguest', verbose_name='guest')),
                ('room', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='room', to='hotel.room', verbose_name='room')),
            ],
            options={
                'ordering': ['-created_at'],
                'abstract': False,
            },
        ),
    ]
