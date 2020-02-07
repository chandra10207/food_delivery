from rest_framework import serializers
from rest_framework.relations import StringRelatedField
from sales.models import Order
from sales.models import OrderItem
from sales.models import OrderItemMeta
from food.serializers import JustFoodSerializer,FoodSerializer, AddonSerializer,FoodInfoSerializer
from restaurant.serializers import JustRestaurantSerializer,RestaurantInfoSerializer



class OrderItemSerializer(serializers.ModelSerializer):

    # food_id = FoodSerializer( read_only=True)

    class Meta:
        # model = models.CustomUser
        model = OrderItem
        fields = ('id','order_id', 'food_id', 'quantity', 'item_price','total_price','addons')


class OrderItemDetailSerializer(serializers.ModelSerializer):

    food_id = FoodInfoSerializer( read_only=True)
    addons = AddonSerializer(read_only=True, many=True)

    class Meta:
        # model = models.CustomUser
        model = OrderItem
        fields = ('id','order_id', 'food_id', 'quantity', 'item_price','total_price','addons')

class OrderSerializer(serializers.ModelSerializer):

    # restaurant = JustRestaurantSerializer(read_only=True)
    # order_items = OrderItemSerializer(many=True,read_only=True)
    order_items = OrderItemDetailSerializer(many=True,read_only=True)

    # some_date = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S.%f%z")

    # food_id = FoodSerializer( read_only=True)

    class Meta:
        # model = models.CustomUser
        model = Order
        ordering = ['id']
        fields = ('id','user_id', 'order_total', 'seller_total', 'driver_total', 'driver', 'order_status', 'created_on','completed_on', 'seller_id', 'order_items')


class OrderDetailSerializer(serializers.ModelSerializer):

    # order_items = OrderItemSerializer(many=True, read_only=True)
    order_items = OrderItemDetailSerializer(many=True,read_only=True)
    seller_id = RestaurantInfoSerializer(read_only=True)

    class Meta:
        # model = models.CustomUser
        model = Order
        fields = ('id','user_id', 'order_total', 'seller_total', 'driver_total', 'driver', 'order_status', 'created_on','completed_on', 'seller_id', 'order_items')


    def update(self, instance, validated_data):
        status = validated_data.get('order_status')
        driver = validated_data.get('driver')
        if instance.order_status != 'completed' and status == 'completed' and instance.driver:
            # breakpoint()
            instance.driver.profile.balance += 5;
            instance.driver.profile.save()
            instance.order_status = status
        else:
            raise serializers.ValidationError("Order already completed")

        # if instance.order_status == 'processing' and status == 'driver_assigned' and driver:
        #     # breakpoint()
        #     instance.driver.profile.balance += 5;
        #     instance.driver.profile.save()
        #     instance.order_status = status
        # else:
        #     raise serializers.ValidationError("Order already completed")

        # profile_data = validated_data.pop('profile')
        # address_data = profile_data.pop('address')
        # address_obj = Address.objects.create(created_by=user)
        # profile_obj = instance.profile
        # # breakpoint()
        # # address_list = list(addresses)
        # profile_obj.phone = profile_data.get('phone', profile_obj.phone)
        # address_obj.unit = address_data.get('unit')
        # address_obj.street_number = address_data.get('street_number')
        # address_obj.street_name = address_data.get('street_name')
        # address_obj.suburb = address_data.get('suburb')
        # address_obj.state = address_data.get('state')
        # address_obj.post_code = address_data.get('post_code')
        # # addresses.created_by = user
        # address_obj.save()
        # profile_obj.address = address_obj
        # profile_obj.save()
        instance.save()
        return instance