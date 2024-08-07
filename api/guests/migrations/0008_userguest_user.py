# Generated by Django 5.0.6 on 2024-06-17 13:30

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guests', '0007_userguest'),
    ]

    operations = [
        migrations.AddField(
            model_name='userguest',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='guest_user', to=settings.AUTH_USER_MODEL, verbose_name='guest_user'),
            preserve_default=False,
        ),
    ]
