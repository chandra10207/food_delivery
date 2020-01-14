from rest_framework import serializers
from rest_framework.relations import StringRelatedField
from sales.models import Order
from sales.models import OrderItem
from sales.models import OrderItemMeta

class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        # model = models.CustomUser
        model = Order
        fields = ('id','user_id', 'order_total', 'seller_total', 'seller_id', 'order_status','created_on','completed_on')




class OrderItemSerializer(serializers.ModelSerializer):

    class Meta:
        # model = models.CustomUser
        model = OrderItem
        fields = ('id','order_id', 'food_id', 'order_item_name', 'seller_id', 'order_status','created_on','completed_on')