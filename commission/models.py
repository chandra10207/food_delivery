from django.db import models

# Create your models here.


class Comission(models.Model):
    comission = models.IntegerField(default=0, verbose_name="Comission")
    is_percentage = models.BooleanField(default=False, verbose_name="Is percentage?")

    def __str__(self):
        if self.is_percentage:
            return "{0}% - Comission".format(self.comission)

        return "${0} - Comission".format(self.comission)

    class Meta:
        verbose_name = "Comission"
        verbose_name_plural = "Comission"
