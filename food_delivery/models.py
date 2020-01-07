from django.db import models
from django.contrib.auth.models import User
from Location.models import Address as UserAddress

# Create your models here.
class UserProfileInfo(models.Model):

    user = models.OneToOneField(User,on_delete=models.CASCADE, related_name='profile')
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)
    address = models.OneToOneField(UserAddress, null=True, related_name='users', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username





