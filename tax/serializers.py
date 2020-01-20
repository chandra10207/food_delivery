from rest_framework import serializers
from rest_framework.validators import ValidationError
from tax.models import Tax

class TaxSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tax
        fields = ( 'tax_percentage',)
    #
    # def create(self, validated_data):
    #
    #     user_id = validated_data.get('user_id')
    #     restaurant_id = validated_data.get('restaurant_id')
    #     # breakpoint()
    #     if StoreFollower.objects.filter(user_id=user_id).filter(restaurant_id=restaurant_id).exists():
    #         content = {'errors': ['Restaurant already added to the favourite list.']}
    #         raise ValidationError(content)
    #     else:
    #         follow = StoreFollower.objects.create(**validated_data)
    #     return follow
