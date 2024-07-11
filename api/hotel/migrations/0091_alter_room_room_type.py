# Generated by Django 5.0.6 on 2024-07-07 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0090_alter_room_room_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='room_type',
            field=models.CharField(choices=[('D', 'DOUBLE'), ('T', 'TRIPLE'), ('S', 'SINGLE')], max_length=2, verbose_name='room type'),
        ),
    ]