# Generated by Django 5.0.6 on 2024-06-16 22:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('guests', '0002_userguest'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userauth',
            name='is_staff',
        ),
    ]
