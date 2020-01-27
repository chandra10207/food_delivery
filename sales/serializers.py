from rest_framework import serializers
from rest_framework.relations import StringRelatedField
from sales.models import Order
from sales.models import OrderItem
from sales.models import OrderItemMeta
from food.serializers import FoodSerializer





class OrderItemSerializer(serializers.ModelSerializer):

    # food_id = FoodSerializer( read_only=True)

    class Meta:
        # model = models.CustomUser
        model = OrderItem
        fields = ('id','order_id', 'food_id', 'order_item_name', 'quantity', 'item_price','total_price','addons')


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        # model = models.CustomUser
        model = Order
        fields = ('id','user_id', 'order_total', 'seller_total', 'seller_id', 'order_status','created_on','completed_on')


class OrderDetailSerializer(serializers.ModelSerializer):

    # order_items = OrderItemSerializer(many=True, read_only=True)
    order_items = OrderItemSerializer(many=True)

    class Meta:
        # model = models.CustomUser
        model = Order
        fields = ('id','user_id', 'order_total', 'seller_total', 'seller_id', 'order_status','created_on','completed_on','order_items')

