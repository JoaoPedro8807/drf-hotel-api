# Generated by Django 5.0.6 on 2024-06-30 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0017_rename_room_id_room_id_remove_room_hotel_instance_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='room_type',
            field=models.CharField(choices=[('T', 'TRIPLE'), ('D', 'DOUBLE'), ('S', 'SINGLE')], max_length=2, verbose_name='room type'),
        ),
    ]