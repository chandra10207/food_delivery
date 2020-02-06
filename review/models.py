from django.db import models
from restaurant.models import Restaurant
from django.contrib.auth.models import User


# Create your models here.
ONE_TO_TEN_RATING_CHOICES = (
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5'),
    (6, '6'),
    (7, '7'),
    (8, '8'),
    (9, '9'),
    (10, '10'),
)

class Review (models.Model):
    user_id = models.ForeignKey(User, related_name='reviews', on_delete=models.CASCADE)
    restaurant_id = models.ForeignKey(Restaurant, related_name='reviews', on_delete=models.CASCADE)
    rating = models.IntegerField(choices=ONE_TO_TEN_RATING_CHOICES, default=1)
    created_on = models.DateTimeField(auto_now_add=True)
    review_title = models.CharField("Title", max_length=140, null=True, blank=True)
    review_text = models.TextField("Review", null=True, blank=True)

    def __str__(self):
        # return self.user_id.first_name
        return "{} - {}".format(str(self.review_title), self.rating)

    class Meta:
        verbose_name = 'Review and Rating'
        unique_together = ('user_id', 'restaurant_id',)



