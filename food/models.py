from django.contrib import admin
from django.db import models
from restaurant.models import Restaurant
from django.contrib.auth.models import User
# from food.middleware import CurrentUserMiddleware

# cms.middleware.user.CurrentUserMiddleware
from django import forms


class Addon(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=255)
    description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    # created_by = models.ForeignKey(User, blank=False, related_name='addons', editable=False, default=CurrentUserMiddleware.get_current_user, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, blank=False, related_name='addons', editable=False, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        # abstract = True
        ordering = ['name']

    def __str__(self):
        return "{} - ${}".format(self.name, self.price)
        # return self.name + self.price



class Food(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=255)
    description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    # author = models.TextField()
    regular_price = models.DecimalField(max_digits=10, decimal_places=2)
    # sale_price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/images/', default='products/images/None/no-img.jpg')
    # restaurant = models.ForeignKey(Restaurant, related_name='foods',editable=False, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, related_name='foods', on_delete=models.CASCADE)
    # owner = models.ForeignKey(User, related_name='foods', editable=False, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, related_name='foods', on_delete=models.CASCADE)
    # toppings = models.ManyToManyField(Addon, blank=True, through='ToppingAmount', related_name='foods')
    addons = models.ManyToManyField(Addon, blank=True)

    # usertest = models.ForeignKey(User, related_name='foods',  on_delete=models.CASCADE)


    def __str__(self):
        # return "{} - {}".format(self.name, self.content)
        return self.name




# class FoodAddon(models.Model):
#     # REGULAR = 1
#     # DOUBLE = 2
#     # TRIPLE = 3
#     # AMOUNT_CHOICES = (
#     #     (REGULAR, 'Regular'),
#     #     (DOUBLE, 'Double'),
#     #     (TRIPLE, 'Triple'),
#     # )
#     food = models.ForeignKey('Food', on_delete=models.SET_NULL, null=True)
#     addon = models.ForeignKey('Addon', on_delete=models.SET_NULL, null=True,)
#     # amount = models.IntegerField(choices=AMOUNT_CHOICES, default=REGULAR)

