# Generated by Django 2.2.9 on 2020-01-08 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0011_auto_20200107_0636'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='email',
            field=models.EmailField(blank=True, max_length=75),
        ),
    ]
