# Generated by Django 5.0.6 on 2024-07-08 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0123_alter_room_room_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='room_type',
            field=models.CharField(choices=[('S', 'SINGLE'), ('D', 'DOUBLE'), ('T', 'TRIPLE')], max_length=2, verbose_name='room type'),
        ),
    ]
