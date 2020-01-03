from rest_framework import serializers
from food.models import Food, Addon


class AddonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Addon
        fields = ("id", "name", "description", "price","created_by")


class JustFoodSerializer(serializers.ModelSerializer):

    class Meta:
        model = Food
        fields = ("id", "name", "description", "regular_price", "image", "restaurant", "owner",'addons')



class FoodSerializer(serializers.ModelSerializer):

    addons = AddonSerializer(many=True, read_only=True)

    class Meta:
        model = Food
        fields = ("id", "name", "description", "regular_price", "image", "restaurant", "owner",'addons')


