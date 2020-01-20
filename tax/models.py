from django.db import models

# Create your models here.

class Tax(models.Model):
    tax_percentage = models.IntegerField(default=0, verbose_name="Comission")
    # is_percentage = models.BooleanField(default=False, verbose_name="Is percentage?")

    def __str__(self):
        # if self.is_percentage:
        #     return "{0}% - Comission".format(self.comission)
        return "{0}% - Tax".format(self.tax_percentage)

    class Meta:
        verbose_name = "Tax"
        verbose_name_plural = "Tax"
