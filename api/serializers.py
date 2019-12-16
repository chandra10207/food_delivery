from rest_framework import serializers
from . import models
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        # model = models.CustomUser
        model = User
        fields = ('id', 'email', 'username')