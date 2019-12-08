from django.db import models


class Restaurant(models.Model):
    name = models.CharField(max_length=42)
    email = models.EmailField(max_length=75)
    website = models.URLField(max_length=200, null=True, blank=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    banner_image = models.ImageField(upload_to='staticfiles/restaurant/images/',
                                     default='staticfiles/restaurant/images/None/no-img.jpg')
    logo = models.ImageField(upload_to='staticfiles/restaurant/images/',
                             default='staticfiles/restaurant/images/None/no-img.jpg')
    owner = models.ForeignKey('auth.User', related_name='restaurant_owner', on_delete=models.CASCADE)
    highlighted = models.TextField()

    class Meta:
        ordering = ['created_on']
