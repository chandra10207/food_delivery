# from django.contrib import admin
# from .models import SaleSummary
#
# @admin.register(SaleSummary)
# class SaleSummaryAdmin(admin.ModelAdmin):
#     change_list_template = 'admin/sale_summary_change_list.html'
#     date_hierarchy = 'created'
#
#     def changelist_view(self, request, extra_context=None):
#         response = super().changelist_view(
#             request,
#             extra_context=extra_context,
#         )
#
#         try:
#             qs = response.context_data['cl'].queryset
#         except (AttributeError, KeyError):
#             return response
#
#         metrics = {
#             'total': Count('id'),
#             'total_sales': Sum('price'),
#         }
#
#         response.context_data['summary'] = list(
#             qs
#                 .values('sale__category__name')
#                 .annotate(**metrics)
#                 .order_by('-total_sales')
#         )
#
#         return response
#
#
# from django.http import HttpResponse
# from django.core import serializers
from django.contrib import admin
from sales.models import Student, Order, OrderItem



def make_published(modeladmin, request, queryset):
    queryset.update(status='p')
make_published.short_description = "Mark selected stories as published"

# @admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    # date_hierarchy = 'pub_date'
    # list_display = ('full_name', 'langugae', 'grades', 'gender')
    list_display = ('full_name', 'grades', 'gender', 'status')
    ordering = ['full_name']
    # list_filter = ('langugae', 'gender', 'grades')
    list_filter = ( 'gender', 'grades')
    save_as = True
    save_on_top = True
    change_list_template = 'change_list_graph.html'
    actions = [make_published]

    # def export_as_json(modeladmin, request, queryset):
    #     response = HttpResponse(content_type="application/json")
    #     serializers.serialize("json", queryset, stream=response)
    #     return response





admin.site.register(Student, StudentAdmin)
admin.site.register(Order)
admin.site.register(OrderItem)