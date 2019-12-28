from django import template
from sales.models import Order


register = template.Library()
@register.simple_tag
def get_sale_completed_count():
    return Order.objects.filter(order_status='completed').count()


