# Generated by Django 5.0.6 on 2024-07-07 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0006_remove_booking_end_date_booking_days'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='end_date',
            field=models.DateField(blank=True, default='2024-06-28'),
            preserve_default=False,
        ),
    ]