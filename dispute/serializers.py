from rest_framework import serializers
from rest_framework.relations import StringRelatedField
from dispute.models import Dispute
from sales.serializers import OrderSerializer, OrderDetailSerializer

class DisputeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Dispute
        fields = ['order_id', 'user_id', 'user_message', "admin_message", "status", 'created_on', 'closed_on']


class DisputeDetailSerializer(serializers.ModelSerializer):

    order_id = OrderDetailSerializer()

    class Meta:
        model = Dispute
        fields = ['order_id', 'user_id', 'user_message', "admin_message", "status", 'created_on', 'closed_on']
