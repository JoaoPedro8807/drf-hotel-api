# Generated by Django 5.0.6 on 2024-07-05 23:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('guests', '0024_delete_abstracthotelmodel'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userguest',
            old_name='id',
            new_name='id_trade',
        ),
    ]
