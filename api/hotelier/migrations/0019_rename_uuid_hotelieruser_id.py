# Generated by Django 5.0.6 on 2024-06-27 18:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotelier', '0018_remove_hotelieruser_abstracthotelmodel_ptr_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hotelieruser',
            old_name='uuid',
            new_name='id',
        ),
    ]
