from rest_framework import serializers
from rest_framework.validators import ValidationError
from review.models import Review
from django.contrib.auth.models import User

class ReviewSerializer(serializers.ModelSerializer):

    name = serializers.SerializerMethodField()

    def get_name(self, obj):
        # breakpoint()
        # user = User.objects.get(pk=obj.user_id.id)
        return "{}".format(obj.user_id.first_name)

    class Meta:
        model = Review
        fields = ('id','user_id', 'restaurant_id', 'rating', 'created_on', 'review_title', 'review_text','name')

    def create(self, validated_data):
        user_id = validated_data.get('user_id')
        restaurant_id = validated_data.get('restaurant_id')
        # breakpoint()
        if Review.objects.filter(user_id=user_id).filter(restaurant_id=restaurant_id).exists():
            content = {'errors': ['Reviews and Rating already exist for this user and restaurant.']}
            raise ValidationError(content)
        else:
            review = Review.objects.create(**validated_data)
        return review
