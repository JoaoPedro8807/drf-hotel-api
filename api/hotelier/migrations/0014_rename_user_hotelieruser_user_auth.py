# Generated by Django 5.0.6 on 2024-06-26 14:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotelier', '0013_alter_hotelieruser_created_at_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hotelieruser',
            old_name='user',
            new_name='user_auth',
        ),
    ]