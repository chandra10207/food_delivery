from django.contrib import admin
from django.db import models
from restaurant.models import Restaurant
from django.contrib.auth.models import User

from django import forms

class ImageUploadForm(forms.Form):
    """Image upload form."""
    image = forms.ImageField()


class Addon(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=255)
    description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        ordering = ['name']

    def __str__(self):
        # return "{} - {}".format(self.name, self.content)
        return self.name



class Food(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=255)
    description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    # author = models.TextField()
    regular_price = models.DecimalField(max_digits=10, decimal_places=2)
    sale_price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/images/', default='products/images/None/no-img.jpg')
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    # toppings = models.ManyToManyField(Addon, blank=True, through='ToppingAmount', related_name='foods')
    # addons = models.ManyToManyField(Addon)

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

