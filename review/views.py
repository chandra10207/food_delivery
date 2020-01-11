from django.shortcuts import render
from rest_framework import generics
from django.http import HttpResponse
from rest_framework.validators import ValidationError
from restaurant.models import Restaurant
from review.models import Review
from review.serializers import ReviewSerializer


# Create your views here.

class ReviewsListAPI(generics.ListCreateAPIView):

    def get_queryset(self):
        # params = self.request.query_params
        # breakpoint()
        restaurant_id = self.request.query_params.get('restaurant_id')
        if restaurant_id:
            if Restaurant.objects.filter(id=restaurant_id).exists():
                queryset = Review.objects.filter(store_id=restaurant_id)
            else:
                content = {'errors': 'store id not exist'}
                raise ValidationError(content)
        else:
            queryset = Review.objects.all()
        return queryset
    # queryset = StoreFollower.objects.all()
    serializer_class = ReviewSerializer


class ReviewsDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


def index(request):
    return HttpResponse('Hello from Store Follower Index page!')