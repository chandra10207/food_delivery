from rest_framework import serializers
from Location.models import Address


class AddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = Address
        fields = ['unit', 'street_number', 'street_name','suburb','state','post_code','created_by']
