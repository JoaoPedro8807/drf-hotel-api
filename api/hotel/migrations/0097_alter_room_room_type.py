# Generated by Django 5.0.6 on 2024-07-07 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0096_hotel_city_hotel_state_hotel_street_hotel_zip_code_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='room_type',
            field=models.CharField(choices=[('D', 'DOUBLE'), ('T', 'TRIPLE'), ('S', 'SINGLE')], max_length=2, verbose_name='room type'),
        ),
    ]
