# Generated by Django 2.2.9 on 2020-02-07 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0012_order_driver'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='driver_total',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]
