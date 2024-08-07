# Generated by Django 5.0.6 on 2024-06-19 19:39

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotelier', '0002_remove_hotelieruser_cnpj'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='hotelieruser',
            name='birthday',
            field=models.DateField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='user birthday'),
        ),
        migrations.AddField(
            model_name='hotelieruser',
            name='document',
            field=models.CharField(default=1, max_length=50, unique=True, verbose_name='CNPJ'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hotelieruser',
            name='first_name',
            field=models.CharField(blank=True, max_length=50, verbose_name='first name'),
        ),
        migrations.AddField(
            model_name='hotelieruser',
            name='last_name',
            field=models.CharField(blank=True, max_length=50, verbose_name='last name'),
        ),
        migrations.AddField(
            model_name='hotelieruser',
            name='phone_number',
            field=models.CharField(blank=True, verbose_name='phone number'),
        ),
        migrations.AddField(
            model_name='hotelieruser',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='hotelier_user', to=settings.AUTH_USER_MODEL, verbose_name='hotelier user'),
            preserve_default=False,
        ),
    ]
