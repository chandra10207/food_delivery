from rest_framework import serializers
from . import models
from django.contrib.auth.models import User

# from rest_auth.registration import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        # model = models.CustomUser
        model = User
        fields = ('id', 'email', 'username')


class CustomRestRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        # model = models.CustomUser
        model = User
        fields = ('id', 'email', 'username', 'first_name', 'last_name', 'password')

