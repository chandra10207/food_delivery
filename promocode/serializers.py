from rest_framework import serializers
from promocode.models import Coupon, Discount
# from food.serializers import FoodSerializer
# from store_follower.serializers import StoreFollowerSerializer


class DiscountSerializer(serializers.ModelSerializer):

    class Meta:
        model = Discount
        fields = ("id", "value", "is_percentage")


class CouponSerializer(serializers.ModelSerializer):

    discount = DiscountSerializer(read_only=True)

    class Meta:
        model = Coupon
        fields = ("id", "code", "discount", "times_used", "created", "ruleset")

#
# class RestaurantSerializer(serializers.ModelSerializer):
#
#     foods = FoodSerializer(many=True, read_only=True)
#     followers = StoreFollowerSerializer(many=True, read_only=True)
#
#     class Meta:
#         model = Restaurant
#         fields = ("id", "name", "content", "restaurant_banner_image", "restaurant_logo", "owner",'foods','followers')