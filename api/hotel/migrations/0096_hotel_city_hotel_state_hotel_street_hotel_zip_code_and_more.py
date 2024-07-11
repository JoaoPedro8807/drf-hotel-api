# Generated by Django 5.0.6 on 2024-07-07 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0095_alter_room_room_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='city',
            field=models.CharField(default=1, max_length=100, verbose_name='hotel city'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hotel',
            name='state',
            field=models.CharField(default=1, max_length=100, verbose_name='hotel state'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hotel',
            name='street',
            field=models.CharField(default='1', max_length=255, verbose_name='hotel street'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hotel',
            name='zip_code',
            field=models.CharField(default='a', max_length=10, verbose_name='hotel zip code'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='room',
            name='room_type',
            field=models.CharField(choices=[('T', 'TRIPLE'), ('D', 'DOUBLE'), ('S', 'SINGLE')], max_length=2, verbose_name='room type'),
        ),
    ]
