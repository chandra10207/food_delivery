from django.contrib import admin
from sales.models import Student, Order, OrderItem, OrderItemMeta
from restaurant.models import Restaurant

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



# @admin.register(Customer)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id','user_id', 'seller_total', 'seller_id',"order_status", 'driver','created_on', 'completed_on']
    search_fields = ['order_status']
    readonly_fields = ['user_id','seller_id','seller_total']
    normaluser_fields = ['user_id', 'seller_total', 'seller_id',"order_status", 'completed_on']
    superuser_fields = ['order_total','driver']
    list_filter = ('order_status', 'driver',)
    # search_fields = ['user_id']
    # autocomplete_fields = ['owner','restaurant','addons']
    # autocomplete_fields = ['addons']
    # list_select_related = ['addons']
    list_per_page = 10

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

admin.site.register(Student, StudentAdmin)
admin.site.register(Order, OrderAdmin)
# admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(OrderItemMeta)