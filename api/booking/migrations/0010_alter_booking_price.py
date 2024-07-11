# Generated by Django 5.0.6 on 2024-07-07 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0009_booking_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, verbose_name='price'),
        ),
    ]
