# Generated by Django 5.0.6 on 2024-06-19 19:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotelier', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hotelieruser',
            name='cnpj',
        ),
    ]
