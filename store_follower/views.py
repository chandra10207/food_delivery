from django.shortcuts import render
from store_follower.models import StoreFollower
from store_follower.serializers import StoreFollowerSerializer
from rest_framework import generics
from django.http import HttpResponse
from django.contrib.auth.models import User
from rest_framework.validators import ValidationError


# Create your views here.

class StoreFollowerListAPI(generics.ListCreateAPIView):

    def get_queryset(self):
        params = self.request.query_params
        # breakpoint()
        user_id = self.request.query_params.get('user_id')
        if user_id:
            if User.objects.filter(id=user_id).exists():
                queryset = StoreFollower.objects.filter(user_id=user_id)
            else:
                content = {'errors': 'user id not exist'}
                raise ValidationError(content)
        else:
            queryset = StoreFollower.objects.all()
        return queryset
    # queryset = StoreFollower.objects.all()
    serializer_class = StoreFollowerSerializer


class StoreFollowerDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = StoreFollower.objects.all()
    serializer_class = StoreFollowerSerializer


def index(request):
    return HttpResponse('Hello from Store Follower Index page!')
