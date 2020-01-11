from rest_framework import serializers
from rest_framework.validators import ValidationError
from review.models import Review

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('id','user_id', 'restaurant_id', 'rating', 'created_on', 'review_title', 'review_text')

    def create(self, validated_data):
        user_id = validated_data.get('user_id')
        restaurant_id = validated_data.get('restaurant_id')
        # breakpoint()
        if Review.objects.filter(user_id=user_id).filter(store_id=restaurant_id).exists():
            content = {'errors': ['Reviews and Rating already provides.']}
            raise ValidationError(content)
        else:
            review = Review.objects.create(**validated_data)
        return review
