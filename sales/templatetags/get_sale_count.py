from django import template
from sales.models import Order
from restaurant.models import Restaurant
from django.db.models import Sum
from store_follower.models import StoreFollower
from food.models import Food
register = template.Library()


@register.simple_tag
def get_sale_count(user):
    if user.is_superuser:
        return Order.objects.count()
    else:
        restaurant = Restaurant.objects.get(owner=user)
        return Order.objects.filter(seller_id=restaurant.id).count()
    # return Order.objects.count()



@register.simple_tag
def get_sale_total(user):
    if user.is_superuser:
        order_total = Order.objects.aggregate(Sum('order_total'))
        # return order_total.order_total__sum
    else:
        restaurant = Restaurant.objects.get(owner=user)
        order_total = Order.objects.filter(seller_id=restaurant.id).aggregate(Sum('seller_total'))
        # breakpoint()
        # if order_total['seller_total__sum'] is None:
        #     order_total.seller_total__sum = 0
        # breakpoint()
        # return order_total.seller_total__sum
    # breakpoint()
    return order_total


@register.simple_tag
def store_followers(user):
    if user.is_superuser:
        store_follower = StoreFollower.objects.all().filter(is_followed=True)
        # order_total = Order.objects.aggregate(Sum('order_total'))
        # return order_total.order_total__sum
    else:
        restaurant = Restaurant.objects.get(owner=user)
        store_follower = restaurant.followers.filter(is_followed=True)
        # breakpoint()

        # order_total = Order.objects.filter(seller_id=restaurant.id).aggregate(Sum('seller_total'))
        # return order_total.seller_total__sum
    # breakpoint()
    return store_follower.count()


@register.simple_tag
def food_count(user):
    if user.is_superuser:
        foods = Food.objects.all()
    else:
        restaurant = Restaurant.objects.get(owner=user)
        foods = restaurant.foods
    return foods.count()


@register.simple_tag
def get_restaurant_total():
    return Restaurant.objects.all().count()

# @register.simple_tag
# def get_restaurant_sale_count(user):
#     if user.is_superuser:
#         return Order.objects.count()
#     else:
#         restaurant = Restaurant.objects.get(owner=user)
#         return Order.objects.filter(seller_id=restaurant.id).count()
        # return Order.objects.filter(order_status=user).count()


@register.simple_tag
def get_restaurant_name(user):
    if user.is_superuser:
        return "Food Delivery"
    else:
        return user.restaurant_owner.name
