# Generated by Django 5.0.6 on 2024-07-08 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0108_alter_room_room_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='room_type',
            field=models.CharField(choices=[('T', 'TRIPLE'), ('S', 'SINGLE'), ('D', 'DOUBLE')], max_length=2, verbose_name='room type'),
        ),
    ]
