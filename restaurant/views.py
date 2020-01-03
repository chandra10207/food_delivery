# from django.shortcuts import render
from restaurant.models import Restaurant
from restaurant.serializers import RestaurantSerializer, JustRestaurantSerializer
from rest_framework import generics
from django.http import HttpResponse


# Create your views here.

class RestaurantList(generics.ListCreateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = JustRestaurantSerializer


class RestaurantDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer


def index(request):
    return HttpResponse('Hello from Restaurant Index page!')