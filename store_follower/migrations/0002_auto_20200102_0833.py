# Generated by Django 3.0 on 2020-01-02 08:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0005_auto_20200102_0822'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('store_follower', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storefollower',
            name='restaurant_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='followers', to='restaurant.Restaurant'),
        ),
        migrations.AlterField(
            model_name='storefollower',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='followed_stores', to=settings.AUTH_USER_MODEL),
        ),
    ]
