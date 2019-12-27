# Generated by Django 3.0 on 2019-12-22 10:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0004_remove_food_sale_price'),
        ('sales', '0005_auto_20191222_1008'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='orderitem',
            options={'verbose_name': 'Order Item'},
        ),
        migrations.AddField(
            model_name='orderitem',
            name='addons',
            field=models.ManyToManyField(blank=True, to='food.Addon'),
        ),
        migrations.CreateModel(
            name='OrderItemMeta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meta_key', models.CharField(max_length=50, verbose_name='Meta Key')),
                ('meta_value', models.CharField(max_length=50, verbose_name='Meta Value')),
                ('order_item_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sales.OrderItem')),
            ],
        ),
    ]
