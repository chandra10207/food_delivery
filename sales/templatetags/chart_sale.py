from django import template
from django.db.models import Count, DateTimeField
from django.db.models.functions import Trunc

from sales.models import Order

register = template.Library()


# @register.assignment_tag
@register.simple_tag
def chart_sale(year):
    context_data = {}
    context_data['summary'] = []
    queryset = Order.objects.filter(completed_on__year=year)
    count = queryset.count()
    # breakpoint()
    if (count == 0):
        return context_data
    summary = queryset.annotate(   period = Trunc('completed_on', 'month',
        output_field=DateTimeField(),
    ), ).values('period').annotate(total=Count('id')).order_by('period')
    context_data = {}
    context_data['summary'] = []
    i = 1  # month iterator
    j = 0  # object iterator
    while (i <= 12):
        if (j < len(summary)):
            x = summary[j]
            if (x['period'].month == i):
                context_data['summary'].append({
                'period': x['period'],
                'total': x['total'],
                'percent': x['total'] / count * 100,
                'month': i,
                })
                i += 1
                j += 1
            else:
                context_data['summary'].append({
                'period': str(i) + ' / ' + str(year)[2:],
                'total': 0,
                'month': i,
                'percent': 0,
                })
                i += 1
        else:
            context_data['summary'].append({
            'period': str(i) + ' / ' + str(year)[2:],'total': 0,
            'percent': 0,
            'month': i,
            })
            i += 1
    return context_data

# register.assignment_tag(chart_sale)
