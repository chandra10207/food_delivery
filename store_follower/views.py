from django.shortcuts import render
from store_follower.models import StoreFollower
from store_follower.serializers import StoreFollowerSerializer
from rest_framework import generics
from django.http import HttpResponse


# Create your views here.

class StoreFollowerListAPI(generics.ListCreateAPIView):
    queryset = StoreFollower.objects.all()
    serializer_class = StoreFollowerSerializer


class StoreFollowerDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = StoreFollower.objects.all()
    serializer_class = StoreFollowerSerializer


def index(request):
    return HttpResponse('Hello from Store Follower Index page!')
