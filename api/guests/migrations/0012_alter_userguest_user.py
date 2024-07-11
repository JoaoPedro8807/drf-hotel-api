# Generated by Django 5.0.6 on 2024-06-19 14:28

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guests', '0011_alter_userguest_options_alter_userguest_document'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userguest',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='especific_user', to=settings.AUTH_USER_MODEL, verbose_name='guest_user'),
        ),
    ]
