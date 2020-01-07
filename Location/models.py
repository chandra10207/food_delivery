from django.db import models

# Create your models here.

class Address(models.Model):

    unit = models.CharField(max_length=20, null=True, blank=True)
    street_number = models.CharField(max_length=20, null=True, blank=True)
    street_name = models.CharField(max_length=50, null=True, blank=True)
    suburb = models.CharField(max_length=50, null=True, blank=True)
    state = models.CharField(max_length=50, null=True, blank=True)
    post_code = models.IntegerField(null=True, blank=True)
    full_address = models.CharField(max_length=100, null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey('auth.User', null=True, related_name='location', on_delete=models.CASCADE)


    class Meta:
        # abstract = True
        ordering = ['suburb']

    def __str__(self):
        return "{}, {} {}, {}, {} " .format(self.unit, self.street_number, self.street_name, self.suburb, self.post_code)
        # return self.name + self.price
