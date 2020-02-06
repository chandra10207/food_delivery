from rest_framework import serializers
from rest_framework.relations import StringRelatedField
from sales.models import Order
from sales.models import OrderItem
from sales.models import OrderItemMeta
from food.serializers import JustFoodSerializer,FoodSerializer, AddonSerializer,FoodInfoSerializer
from restaurant.serializers import JustRestaurantSerializer,RestaurantInfoSerializer



class OrderItemSerializer(serializers.ModelSerializer):

    # food_id = FoodSerializer( read_only=True)

    class Meta:
        # model = models.CustomUser
        model = OrderItem
        fields = ('id','order_id', 'food_id', 'quantity', 'item_price','total_price','addons')


class OrderItemDetailSerializer(serializers.ModelSerializer):

    food_id = FoodInfoSerializer( read_only=True)
    addons = AddonSerializer(read_only=True, many=True)

    class Meta:
        # model = models.CustomUser
        model = OrderItem
        fields = ('id','order_id', 'food_id', 'quantity', 'item_price','total_price','addons')

class OrderSerializer(serializers.ModelSerializer):

    # restaurant = JustRestaurantSerializer(read_only=True)
    # order_items = OrderItemSerializer(many=True,read_only=True)
    order_items = OrderItemDetailSerializer(many=True,read_only=True)

    # some_date = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S.%f%z")

    # food_id = FoodSerializer( read_only=True)

    class Meta:
        # model = models.CustomUser
        model = Order
        ordering = ['id']
        fields = ('id','user_id', 'order_total', 'seller_total', 'driver', 'order_status', 'created_on','completed_on', 'seller_id', 'order_items')


class OrderDetailSerializer(serializers.ModelSerializer):

    # order_items = OrderItemSerializer(many=True, read_only=True)
    order_items = OrderItemDetailSerializer(many=True,read_only=True)
    seller_id = RestaurantInfoSerializer(read_only=True)

    class Meta:
        # model = models.CustomUser
        model = Order
        fields = ('id','user_id', 'order_total', 'seller_total', 'driver', 'order_status', 'created_on','completed_on', 'seller_id', 'order_items')

