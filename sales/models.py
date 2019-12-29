# from django.db import models
#
# # Create your models here.
#
#
# class SaleSummary(Sale):
#     class Meta:
#         proxy = True
#         verbose_name = 'Sale Summary'
#         verbose_name_plural = 'Sales Summary'

from django.db import models
from django.contrib.auth.models import User
from django.db.models.functions import datetime

from restaurant.models import Restaurant
from food.models import Food, Addon


MALE, FEMALE = range(2)
GENDER = (
    (MALE, 'MALE'),
    (FEMALE, 'FEMALE')
)

CHINESE, SPANISH, ENGLISH, FRENCH, HINDI, ARABIC, RUSSIAN = range(7)
LANGUAGES = (
    (CHINESE, 'CHINESE'),
    (SPANISH, 'SPANISH'),
    (ENGLISH, 'ENGLISH'),
    (FRENCH, 'FRENCH'),
    (HINDI, 'HINDI'),
    (ARABIC, 'ARABIC'),
    (RUSSIAN, 'RUSSIAN'),
)

STATUS_CHOICES = (
    ('d', 'Draft'),
    ('p', 'Published'),
    ('w', 'Withdrawn'),
)

ORDER_STATUS = (
    ('pending_payment', 'Pending Payment'),
    ('processing', 'Processing'),
    ('accepted', 'Accepted'),
    ('driver_assigned', 'Driver Assigned'),
    ('cancel', 'Canceled'),
    ('completed', 'Completed'),
)



class Student(models.Model):
    full_name = models.CharField('Full Name', max_length=50)
    gender = models.PositiveSmallIntegerField('Gender', choices=GENDER, default=MALE)
    language = models.PositiveSmallIntegerField('Language', choices=LANGUAGES, default=ENGLISH)
    grades = models.CharField('Grades', max_length=2)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES , default='p')

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = ('Student')


class Order(models.Model):
    user_id = models.ForeignKey(User, related_name='images', on_delete=models.CASCADE)
    order_total = models.DecimalField(max_digits=10, decimal_places=2)
    seller_total = models.DecimalField(max_digits=10, decimal_places=2)
    seller_id = models.ForeignKey(Restaurant, related_name='restaurant', on_delete=models.CASCADE)
    order_status =  models.CharField(max_length=40, choices=ORDER_STATUS, default='processing')
    created_on = models.DateTimeField(auto_now_add=True)
    completed_on = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        # return self.user_id.first_name
        return "{} - {}".format(str(self.id), self.user_id.first_name)

    class Meta:
        verbose_name = ('Order')


class OrderItem(models.Model):
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    food_id = models.ForeignKey(Food, related_name='food', on_delete=models.CASCADE)
    order_item_name = models.CharField('Item Name', max_length=50)
    quantity = models.PositiveSmallIntegerField('Quantiy', default=1)
    item_price = models.DecimalField(max_digits=10, decimal_places=2)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    addons = models.ManyToManyField(Addon, blank=True)

    def __str__(self):
        return str(self.order_id)

    class Meta:
        verbose_name = ('Order Item')


class OrderItemMeta(models.Model):
    order_item_id = models.ForeignKey(OrderItem, on_delete=models.CASCADE)
    meta_key = models.CharField('Meta Key', max_length=50)
    meta_value = models.CharField('Meta Value', max_length=50)










