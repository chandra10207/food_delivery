from django.db import models
# from address.models import AddressField
from django import forms
# from django_google_maps import fields as map_fields
from Location.models import Address
from django.utils.html import mark_safe
from django.conf import settings
from django.db.models import Avg
from decimal import *

class ImageUploadForm(forms.Form):
    """Image upload form."""
    image = forms.ImageField()

class Restaurant(models.Model):
    name = models.CharField(max_length=42)
    newfields = models.CharField(max_length=42, null=True, blank=True)
    restaurant_address = models.CharField("Address", max_length=42, null=True, blank=True)
    email = models.EmailField(max_length=75, blank=True)
    website = models.URLField(max_length=200, null=True, blank=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    # banner_image = models.ImageField(upload_to='restaurant/images/', default='restaurant/images/None/no-img.jpg')
    # logo = models.ImageField(upload_to='restaurant/images/', default='restaurant/images/None/no-img.jpg')
    restaurant_banner_image = models.ImageField("Banner Image", upload_to='restaurant/images/',blank=True)
    restaurant_logo = models.ImageField("Logo", upload_to='restaurant/images/',blank=True)
    # owner = models.ForeignKey('auth.User', related_name='restaurant_owner', editable=False, on_delete=models.CASCADE)
    owner = models.ForeignKey('auth.User', related_name='restaurant_owner', on_delete=models.CASCADE)
    address = models.OneToOneField(Address, null=True, related_name='restaurants', on_delete=models.CASCADE)
    # address = map_fields.AddressField(max_length=200, null=True, blank=True)
    # geolocation = map_fields.GeoLocationField(max_length=100, null=True, blank=True)
    # from django_google_maps import fields as map_fields
    # follower = models.ManyToManyField('auth.User', blank=True)
    # address1 = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'id': "autocomplete"}))
    # address2 = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'id': "autocomplete"}))
    # address1 = AddressField(blank=True, null=True)
    # address2 = AddressField(related_name='+', blank=True, null=True)
    # highlighted = models.TextField()

    def restaurant_logo_tag(self):
        return mark_safe('<img class="user-image img-circle" src="%s%s" width="80" height="80" />' % (settings.MEDIA_URL , self.restaurant_logo))
    restaurant_logo_tag.short_description = 'Restaurant Logo'

    # def average_rating(self):
    #     # breakpoint()
    #     avg =  self.reviews.aggregate(Avg('rating'))
    #     breakpoint()
    #     return Decimal(avg)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['created_on']
        # permissions = (
        #     ('read_item','Can read item'),
        # )
