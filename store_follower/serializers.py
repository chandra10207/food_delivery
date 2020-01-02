from rest_framework import serializers
from store_follower.models import StoreFollower


class StoreFollowerSerializer(serializers.ModelSerializer):

    class Meta:
        model = StoreFollower
        fields = ('user_id', 'follower_name', 'restaurant_id', 'restaurant_name', 'followed_on')

