# Generated by Django 5.0.6 on 2024-07-15 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0137_alter_room_room_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='city',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='hotel city'),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='state',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='hotel state'),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='street',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='hotel street'),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='zip_code',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='hotel zip code'),
        ),
        migrations.AlterField(
            model_name='room',
            name='room_type',
            field=models.CharField(choices=[('S', 'SINGLE'), ('D', 'DOUBLE'), ('T', 'TRIPLE')], max_length=2, verbose_name='room type'),
        ),
    ]