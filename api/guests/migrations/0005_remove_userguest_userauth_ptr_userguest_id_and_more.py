# Generated by Django 5.0.6 on 2024-06-17 13:11

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guests', '0004_userauth_is_staff'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userguest',
            name='userauth_ptr',
        ),
        migrations.AddField(
            model_name='userguest',
            name='guest_id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='User Guest ID'),
            preserve_default=False
        ),
        migrations.AlterField(
            model_name='userguest',
            name='birthday',
            field=models.DateField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='user birthday'),
        ),
    ]
