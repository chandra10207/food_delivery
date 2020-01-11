# Generated by Django 2.2.9 on 2020-01-11 08:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('restaurant', '0012_auto_20200108_0702'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')], default=1)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('review_title', models.CharField(max_length=140, null=True, verbose_name='Title')),
                ('review_text', models.TextField(null=True, verbose_name='Review')),
                ('store_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='restaurant.Restaurant')),
                ('user_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Review and Rating',
            },
        ),
    ]
