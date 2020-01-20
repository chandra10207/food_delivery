# Generated by Django 2.2.9 on 2020-01-20 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tax',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tax_percentage', models.IntegerField(default=0, verbose_name='Comission')),
            ],
            options={
                'verbose_name': 'Tax',
                'verbose_name_plural': 'Tax',
            },
        ),
    ]
