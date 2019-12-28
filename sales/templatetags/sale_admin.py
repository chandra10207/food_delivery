from django import template
from sales.models import Order

register = template.Library()


@register.inclusion_tag('sale_admin.html')
def sale_admin():
    data = Order.objects.all()
    return {'variable': data}


