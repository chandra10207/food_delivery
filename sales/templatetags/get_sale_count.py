from django import template
from sales.models import Order
register = template.Library()


@register.simple_tag
def get_sale_count():
    return Order.objects.count()

@register.simple_tag
def get_restaurant_sale_count(user):
    if user.is_superuser:
        return Order.objects.count()
    else:
        return Order.objects.filter(order_status='completed').count()


@register.simple_tag
def get_restaurant_name(user):
    if user.is_superuser:
        return "Food Delivery"
    else:
        return user.restaurant_owner.name
