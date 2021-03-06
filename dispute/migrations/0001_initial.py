# Generated by Django 2.2.9 on 2020-01-27 08:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sales', '0010_auto_20200120_2251'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Dispute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_message', models.TextField()),
                ('admin_message', models.TextField()),
                ('status', models.CharField(choices=[('open', 'Open'), ('closed', 'Closed')], default='open', max_length=40)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('completed_on', models.DateTimeField(blank=True, null=True)),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dispute', to='sales.Order')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='disputes', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Disputes',
            },
        ),
    ]
