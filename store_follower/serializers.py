from rest_framework import serializers
from store_follower.models import StoreFollower
from rest_framework.validators import ValidationError

class StoreFollowerSerializer(serializers.ModelSerializer):

    class Meta:
        model = StoreFollower
        fields = ( 'id', 'user_id', 'follower_name', 'restaurant_id', 'restaurant_name', 'followed_on')

    def create(self, validated_data):

        user_id = validated_data.get('user_id')
        restaurant_id = validated_data.get('restaurant_id')
        # breakpoint()
        if StoreFollower.objects.filter(user_id=user_id).filter(restaurant_id=restaurant_id).exists():
            content = {'errors': ['Restaurant already added to the favourite list.']}
            raise ValidationError(content)
        else:
            follow = StoreFollower.objects.create(**validated_data)
        return follow
