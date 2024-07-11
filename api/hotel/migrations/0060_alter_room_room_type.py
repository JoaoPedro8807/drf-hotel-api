# Generated by Django 5.0.6 on 2024-07-05 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0059_alter_room_room_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='room_type',
            field=models.CharField(choices=[('S', 'SINGLE'), ('T', 'TRIPLE'), ('D', 'DOUBLE')], max_length=2, verbose_name='room type'),
        ),
    ]