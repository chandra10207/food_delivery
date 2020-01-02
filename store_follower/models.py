from django.db import models
from restaurant.models import Restaurant

# Create your models here.

class StoreFollower(models.Model):
    follower_name = models.CharField(max_length=42, null=True, blank=True)
    restaurant_name = models.CharField(max_length=42, null=True, blank=True)
    followed_on = models.DateTimeField(auto_now_add=True)
    is_followed = models.BooleanField(default=True)
    # user_id = models.ForeignKey('auth.User', related_name='followed_stores', editable=False, on_delete=models.CASCADE)
    user_id = models.ForeignKey('auth.User', related_name='followed_stores', on_delete=models.CASCADE, verbose_name='User')
    # restaurant_id = models.ForeignKey(Restaurant, related_name='followers', editable=False, on_delete=models.CASCADE)
    restaurant_id = models.ForeignKey(Restaurant, related_name='followers', on_delete=models.CASCADE,verbose_name='Restaurant')

    def __str__(self):
        # return "{} Followed {} From {}".format(self.user_id, self.restaurant_id, self.followed_on)
        return str(self.user_id)
