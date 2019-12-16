from rest_framework import generics

from . import models
from . import serializers
from django.contrib.auth.models import User


class UserListView(generics.ListAPIView):
    # queryset = models.CustomUser.objects.all()
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer