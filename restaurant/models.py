from django.db import models
# from django import forms
#
# class ImageUploadForm(forms.Form):
#     """Image upload form."""
#     image = forms.ImageField()

class Restaurant(models.Model):
    name = models.CharField(max_length=42)
    restaurant_address = models.CharField(max_length=42)
    email = models.EmailField(max_length=75)
    website = models.URLField(max_length=200, null=True, blank=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    # banner_image = models.ImageField(upload_to='restaurant/images/', default='restaurant/images/None/no-img.jpg')
    # logo = models.ImageField(upload_to='restaurant/images/', default='restaurant/images/None/no-img.jpg')
    restaurant_banner_image = models.ImageField(upload_to='restaurant/images/',blank=True)
    restaurant_logo = models.ImageField(upload_to='restaurant/images/',blank=True)
    owner = models.ForeignKey('auth.User', related_name='restaurant_owner', on_delete=models.CASCADE)
    # highlighted = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['created_on']
