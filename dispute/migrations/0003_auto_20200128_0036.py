# Generated by Django 2.2.9 on 2020-01-28 00:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dispute', '0002_auto_20200127_1031'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dispute',
            options={'verbose_name': 'Dispute'},
        ),
        migrations.AlterField(
            model_name='dispute',
            name='admin_message',
            field=models.TextField(blank=True, null=True),
        ),
    ]
