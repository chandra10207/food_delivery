from rest_framework import serializers
from rest_framework.relations import StringRelatedField
from sales.models import Order
from sales.models import OrderItem
from sales.models import OrderItemMeta

class OrderSerializer(serializers.ModelSerializer):

    # def get_queryset(self):
    #     params = self.request.query_params
    #     breakpoint()
    #     user_id = self.request.query_params.get('user_id')
    #
    #     # latitude = self.request.query_params.get('latitude')
    #     # radius = self.request.query_params.get('radius')
    #     #
    #     # location = Point(longitude, latitude)
    #     if user_id:
    #         queryset = Order.objects.filter(user_id=user_id)
    #     return queryset

    class Meta:
        # model = models.CustomUser
        model = Order
        fields = ('id','user_id', 'order_total', 'seller_total', 'seller_id', 'order_status','created_on','completed_on')