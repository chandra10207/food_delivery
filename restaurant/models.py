from django.db import models
# from address.models import AddressField
from django import forms
# from django_google_maps import fields as map_fields



class ImageUploadForm(forms.Form):
    """Image upload form."""
    image = forms.ImageField()

class Restaurant(models.Model):
    name = models.CharField(max_length=42)
    restaurant_address = models.CharField(max_length=42, null=True, blank=True)
    email = models.EmailField(max_length=75)
    website = models.URLField(max_length=200, null=True, blank=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    # banner_image = models.ImageField(upload_to='restaurant/images/', default='restaurant/images/None/no-img.jpg')
    # logo = models.ImageField(upload_to='restaurant/images/', default='restaurant/images/None/no-img.jpg')
    restaurant_banner_image = models.ImageField(upload_to='restaurant/images/',blank=True)
    restaurant_logo = models.ImageField(upload_to='restaurant/images/',blank=True)
    owner = models.ForeignKey('auth.User', related_name='restaurant_owner', editable=False, on_delete=models.CASCADE)
    # address = map_fields.AddressField(max_length=200, null=True, blank=True)
    # geolocation = map_fields.GeoLocationField(max_length=100, null=True, blank=True)
    # from django_google_maps import fields as map_fields
    # follower = models.ManyToManyField('auth.User', blank=True)
    # address1 = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'id': "autocomplete"}))
    # address2 = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'id': "autocomplete"}))
    # address1 = AddressField(blank=True, null=True)
    # address2 = AddressField(related_name='+', blank=True, null=True)
    # highlighted = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['created_on']
        # permissions = (
        #     ('read_item','Can read item'),
        # )
