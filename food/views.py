from django.shortcuts import render
from food.models import Food
from food.serializers import FoodSerializer, JustFoodSerializer
from rest_framework import generics
from django.http import HttpResponse


# Create your views here.

class FoodsList(generics.ListCreateAPIView):
    queryset = Food.objects.all()
    serializer_class = JustFoodSerializer


class FoodDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer


def index(request):
    return HttpResponse('Hello from Foods Index page!')
