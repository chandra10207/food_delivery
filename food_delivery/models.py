from django.db import models
from django.contrib.auth.models import User
from Location.models import Address as UserAddress
from gettingstarted.settings import MEDIA_URL
# Create your models here.


class UserProfileInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, related_name='profile')
    portfolio_site = models.URLField(blank=True)
    # firstname = models.CharField(max_length=50, null=True, blank=True)
    # lastname = models.CharField(max_length=50, null=True, blank=True)
    phone = models.CharField(max_length=50, null=True, blank=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)
    address = models.OneToOneField(UserAddress, null=True, related_name='users', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

    def get_profile_pic_url(self):
        return "{}{}".format(MEDIA_URL, self.profile_pic)





