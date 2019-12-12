from rest_framework import serializers
from food.models import Food


class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = ("id", "name", "name", "description", "regular_price", "sale_price", "sale_price", "image", "restaurant", "owner")