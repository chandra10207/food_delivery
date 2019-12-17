from rest_framework import serializers
from rest_framework.relations import StringRelatedField

from restaurant.models import Restaurant
from food.serializers import FoodSerializer

class RestaurantSerializer(serializers.ModelSerializer):

    foods = FoodSerializer(many=True, read_only=True)

    class Meta:
        model = Restaurant
        fields = ("id", "name", "content", "banner_image", "logo", "owner",'foods')