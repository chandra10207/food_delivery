from rest_framework import serializers
from rest_framework.relations import StringRelatedField

from restaurant.models import Restaurant
from food.serializers import FoodSerializer
from store_follower.serializers import StoreFollowerSerializer
from Location.serializers import AddressSerializer
from review.serializers import ReviewSerializer


class RestaurantInfoSerializer(serializers.ModelSerializer):
    # average_rating_value = serializers.DecimalField(source='average_rating',max_digits=10, decimal_places=2)

    class Meta:
        model = Restaurant
        fields = ("id", "name", "content", "restaurant_banner_image", "restaurant_logo", "owner")


class JustRestaurantSerializer(serializers.ModelSerializer):
    # average_rating_value = serializers.DecimalField(source='average_rating',max_digits=10, decimal_places=2)

    class Meta:
        model = Restaurant
        fields = ("id", "name", "content", "restaurant_banner_image", "restaurant_logo", "owner", 'foods','followers','reviews')


class RestaurantSerializer(serializers.ModelSerializer):

    foods = FoodSerializer(many=True, read_only=True)
    followers = StoreFollowerSerializer(many=True, read_only=True)
    address = AddressSerializer(read_only=True)
    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Restaurant
        fields = ("id", "name", "content", "restaurant_banner_image", "restaurant_logo", "owner",'address','foods','followers','reviews')