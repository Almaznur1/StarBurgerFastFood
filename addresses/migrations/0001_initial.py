# Generated by Django 3.2.15 on 2023-10-03 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MapPoint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=200, verbose_name='адрес')),
                ('lat', models.FloatField(blank=True, null=True, verbose_name='Широта')),
                ('lon', models.FloatField(blank=True, null=True, verbose_name='Долгота')),
                ('coordinates_update_date', models.DateField(auto_now=True, verbose_name='дата последнего обновления координат')),
            ],
        ),
    ]
