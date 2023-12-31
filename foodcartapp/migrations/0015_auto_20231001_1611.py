# Generated by Django 3.2.15 on 2023-10-01 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodcartapp', '0014_auto_20230930_1114'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='lat',
            field=models.FloatField(default=0, verbose_name='Широта'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='lon',
            field=models.FloatField(default=0, verbose_name='Долгота'),
            preserve_default=False,
        ),
    ]
