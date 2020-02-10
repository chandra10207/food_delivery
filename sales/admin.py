from django.contrib import admin
from django.utils.safestring import mark_safe

from sales.models import Student, Order, OrderItem, OrderItemMeta
from restaurant.models import Restaurant
from  sales.models import OrderItem
from django.contrib.auth.models import User
from django.utils.html import format_html
from django.urls import reverse

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

# class UserInline(admin.TabularInline):
#     model = Restaurant

# class CategoryAdmin(admin.ModelAdmin):
#     inlines = [
#         UserInline,
#     ]


class OrderItemline(admin.TabularInline):
    model = OrderItem
    readonly_fields = ('food_id', 'quantity', 'total_price',)
    fields = ('food_id', 'quantity', 'total_price',)
    raw_id_fields = ("food_id",)

    def get_extra(self, request, obj=None, **kwargs):
        extra = 0
        # if obj:
        #     return extra - obj.orderitem_set.count()
        return extra

    def has_delete_permission(self, request, obj=None, **kwargs):
        if obj:
            # return extra - obj.orderitem_set.count()
            return False;

    def has_add_permission(self, request, obj=None, **kwargs):
        if obj:
            # return extra - obj.orderitem_set.count()
            return False;

# def linkify(field_name):
#     """
#     Converts a foreign key value into clickable links.
#
#     If field_name is 'parent', link text will be str(obj.parent)
#     Link will be admin url for the admin url for obj.parent.id:change
#     """
#     def _linkify(obj):
#         app_label = obj._meta.app_label
#         linked_obj = getattr(obj, field_name)
#         model_name = linked_obj._meta.model_name
#         view_name = f"admin:{app_label}_{model_name}_change"
#         link_url = reverse(view_name, args=[linked_obj.id])
#         return format_html('<a href="{}">{}</a>', link_url, linked_obj)
#
#     _linkify.short_description = field_name # Sets column name
#     return _linkify


# @admin.register(Customer)
class OrderAdmin(admin.ModelAdmin):
    # change_list_template = 'change_form.html'
    list_display = ['id','user_id', 'order_total', 'seller_id',"order_status", 'driver','driver_phone','created_on', 'completed_on',
        # linkify(field_name="user_id"),
        # linkify(field_name="driver"),
                    ]
    search_fields = ['order_status']
    readonly_fields = ['user_id','seller_id'
        ,'seller_total']
    normaluser_fields = ['user_id', 'order_total', 'driver', "order_status", 'completed_on']
    superuser_fields = ['order_total','seller_id',]
    list_filter = ('order_status',)
    # search_fields = ['user_id']
    # autocomplete_fields = ['owner','restaurant','addons']
    # autocomplete_fields = ['addons']
    # list_select_related = ['addons']
    list_per_page = 10
    inlines = [
        OrderItemline,
    ]
    # fieldsets = default_employee_fieldset

    def driver_link(self, order):
        if order.driver:
            url = reverse("admin:auth_user_change", args=[order.driver.id])
            link = '<a href="%s">%s</a>' % (url, order.driver.username)
            return mark_safe(link)
        else:
            return "-"
    driver_link.short_description = 'Driver'

    def driver_phone(self, order):
        if order.driver:
            phone = order.driver.profile.phone
            # link = '<a href="%s">%s</a>' % (url, order.driver.username)
            return phone
        else:
            return "-"
    driver_link.short_description = 'Driver'


    def get_formsets_with_inlines(self, request, obj=None):
        for inline in self.get_inline_instances(request, obj):
            # hide MyInline in the add view
            if not isinstance(inline, OrderItemline) or obj is not None:
                yield inline.get_formset(request, obj), inline

    def get_form(self, request, obj=None, **kwargs):
        if request.user.is_superuser:
            self.fields = self.normaluser_fields + self.superuser_fields
        else:
            self.fields = self.normaluser_fields
        return super(OrderAdmin, self).get_form(request, obj, **kwargs)

    def get_readonly_fields(self, request, obj=None):
        if request.user.is_superuser:
            return []
        return self.readonly_fields
    #
    #
    # def changelist_view(self, request, extra_context=None):
    #     if request.user.is_superuser:
    #         self.list_display = ['user_id', 'seller_total', 'seller_id',"order_status"]
    #     else:
    #         self.list_display = ['user_id', 'seller_total', 'seller_id',"order_status"]
    #
    # def get_form(self, request, obj=None, **kwargs):
    #     self.exclude = []
    #     if request.user.is_superuser:
    #         self.exclude = []
    #         # self.fieldsets = self.fieldsets_user + self.fieldsets_superuser
    #     else:
    #         self.exclude.extend(['seller_total', ])
    #         # self.fieldsets = self.fieldsets_user
    #     return super(OrderAdmin, self).get_form(request, obj, **kwargs)

    # def get_readonly_fields(self, request, obj=None):
    #     if request.user.is_staff:
    #         if request.user.is_superuser:
    #             return []
    #         else:
    #             return [f.name for f in self.model._meta.fields]


    #     return ["owner"]
    #     # if obj:
    #     #     return ["name", "category"]
    #     # else:
    #     #     return []

    # def save_model(self, request, obj, form, change):
    #     """When creating a new object, set the creator field.
    #     """
    #     if not change:
    #         obj.created_by = request.user
    #     obj.save()

    def get_queryset(self, request):
        qs = super(OrderAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        else:
            restaurant = Restaurant.objects.get(owner=request.user)
            return qs.filter(seller_id=restaurant.id)

# admin.site.register(Student, StudentAdmin)
admin.site.register(Order, OrderAdmin)
# admin.site.register(Order)
# admin.site.register(OrderItem)
@admin.register(OrderItem)
class StudentAdmin(admin.ModelAdmin):
    # date_hierarchy = 'pub_date'
    # list_display = ('full_name', 'langugae', 'grades', 'gender')
    list_display = ('order_id', 'food_id', 'quantity','total_price')
    ordering = ['order_id']
    # list_filter = ('langugae', 'gender', 'grades')
    list_filter = ( 'order_id',)
    save_as = True
    save_on_top = True
    # change_list_template = 'change_list_graph.html'
    # actions = [make_published]


admin.site.register(OrderItemMeta)