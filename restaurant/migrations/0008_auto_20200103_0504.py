# Generated by Django 2.2.9 on 2020-01-03 05:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0007_restaurant_newfields'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='restaurant_owner', to=settings.AUTH_USER_MODEL),
        ),
    ]
