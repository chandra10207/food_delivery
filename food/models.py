from django.db import models
from restaurant.models import Restaurant
from django.contrib.auth.models import User

from django import forms

class ImageUploadForm(forms.Form):
    """Image upload form."""
    image = forms.ImageField()

class Food(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=255)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    # author = models.TextField()
    regular_price = models.DecimalField(max_digits=10, decimal_places=2)
    sale_price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='assets/images/', default='assets/images/None/no-img.jpg')
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return "{} - {}".format(self.name, self.content)
