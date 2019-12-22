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
from restaurant.models import Restaurant

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
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    order_total = models.DecimalField(max_digits=10, decimal_places=2)
    seller_total = models.DecimalField(max_digits=10, decimal_places=2)
    seller_id = models.ForeignKey(Restaurant, related_name='restaurant', on_delete=models.CASCADE)
    order_status =  models.CharField(max_length=40, choices=ORDER_STATUS, default='processing')

    def __str__(self):
        return self.id

    class Meta:
        verbose_name = ('Order')


# class OrderItem(models.Model):
#     order_id = models.ForeignKey(Order, on_delete=models.CASCADE)

