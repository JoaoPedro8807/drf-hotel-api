# Generated by Django 5.0.6 on 2024-06-17 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guests', '0009_remove_userauth_first_name_remove_userauth_last_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userauth',
            name='type_user',
            field=models.CharField(choices=[('GS', 'Guest'), ('HL', 'Hotelier')], verbose_name='type of user, hotelier or guest'),
        ),
    ]
