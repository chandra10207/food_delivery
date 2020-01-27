from rest_framework import serializers
from food_delivery.models import UserProfileInfo
from Location.serializers import AddressSerializer

class ProfileSerializer(serializers.ModelSerializer):

    address = AddressSerializer()

    class Meta:
        model = UserProfileInfo
        # fields = "__all__"
        fields = ['id', 'phone', 'portfolio_site', 'profile_pic', 'address']
