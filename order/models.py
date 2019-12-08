from django.db import models
from food.models import Food
from django.contrib.auth.models import User


class Order(models.Model):
    order_id = models.IntegerField(primary_key=True)
    food_id = models.ForeignKey(Food, on_delete=models.CASCADE)
    customer_id = models.ForeignKey(User, on_delete=models.CASCADE)


