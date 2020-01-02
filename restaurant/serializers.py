from rest_framework import serializers
from rest_framework.relations import StringRelatedField

from restaurant.models import Restaurant
from food.serializers import FoodSerializer
from store_follower.serializers import StoreFollowerSerializer

class RestaurantSerializer(serializers.ModelSerializer):

    foods = FoodSerializer(many=True, read_only=True)
    # store_follower = StoreFollowerSerializer(many=True, read_only=True)

    class Meta:
        model = Restaurant
        fields = ("id", "name", "content", "restaurant_banner_image", "restaurant_logo", "owner",'foods')