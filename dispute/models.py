from django.db import models
from django.contrib.auth.models import User
from sales.models import Order

DISPUTE_STATUS = (
    ('open', 'Open'),
    ('closed', 'Closed'),
)

# Create your models here.
class Dispute(models.Model):
    user_id = models.ForeignKey(User, related_name='disputes', on_delete=models.CASCADE)
    order_id = models.ForeignKey(Order, related_name='dispute', on_delete=models.CASCADE)
    user_message = models.TextField()
    admin_message = models.TextField()
    status =  models.CharField(max_length=40, choices=DISPUTE_STATUS, default='open')
    created_on = models.DateTimeField(auto_now_add=True)
    closed_on = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        # return self.user_id.first_name
        return "Order: {} - User: {}".format(str(self.order_id), self.user_id.first_name)

    def get_restaurant_id(self):
        return self.order_id.seller_id

    class Meta:
        verbose_name = ('Dispute')