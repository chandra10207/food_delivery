# Generated by Django 2.2.9 on 2020-01-11 11:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0002_auto_20200111_1147'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='store_id',
            new_name='restaurant_id',
        ),
    ]
