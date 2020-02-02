from rest_framework import serializers
from rest_framework.relations import StringRelatedField
from sales.models import Order
from sales.models import OrderItem
from sales.models import OrderItemMeta
from food.serializers import JustFoodSerializer,FoodSerializer
from restaurant.serializers import JustRestaurantSerializer


class OrderItemSerializer(serializers.ModelSerializer):

    # food_id = FoodSerializer( read_only=True)

    class Meta:
        # model = models.CustomUser
        model = OrderItem
        fields = ('id','order_id', 'food_id', 'quantity', 'item_price','total_price','addons')


class OrderItemDetailSerializer(serializers.ModelSerializer):

    food_id = FoodSerializer( read_only=True)

    class Meta:
        # model = models.CustomUser
        model = OrderItem
        fields = ('id','order_id', 'food_id', 'quantity', 'item_price','total_price','addons')

class OrderSerializer(serializers.ModelSerializer):

    # restaurant = JustRestaurantSerializer(read_only=True)
    order_items = OrderItemSerializer(many=True,read_only=True)

    # food_id = FoodSerializer( read_only=True)

    class Meta:
        # model = models.CustomUser
        model = Order
        fields = ('id','user_id', 'order_total', 'seller_total', 'seller_id', 'order_status', 'order_items', 'created_on','completed_on')


class OrderDetailSerializer(serializers.ModelSerializer):

    # order_items = OrderItemSerializer(many=True, read_only=True)
    order_items = OrderItemDetailSerializer(many=True,read_only=True)
    seller_id = JustRestaurantSerializer(read_only=True)

    class Meta:
        # model = models.CustomUser
        model = Order
        fields = ('id','user_id', 'order_total', 'seller_total', 'seller_id', 'order_status','created_on','completed_on','order_items')

