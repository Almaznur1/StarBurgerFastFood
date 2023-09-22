# Generated by Django 3.2.15 on 2023-09-22 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodcartapp', '0007_auto_20230921_1132'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='comment',
            field=models.TextField(default='', verbose_name='комментарий менеджера'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('MANAGER', 'Необработанный'), ('RESTAURANT', 'В ресторане'), ('COURIER', 'У курьера'), ('COMPLETED', 'Выполнен')], db_index=True, max_length=10, verbose_name='статус заказа'),
        ),
    ]