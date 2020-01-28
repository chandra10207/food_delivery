from django.contrib import admin
from dispute.models import Dispute
from restaurant.models import Restaurant
# Register your models here.




class DisputeAdmin(admin.ModelAdmin):
    list_display = ['order_id', 'user_id', 'user_message', "admin_message", "status", 'created_on', 'closed_on']
    search_fields = ['user_message']
    readonly_fields = ['user_id','order_id','user_message',]
    # normaluser_fields = ['user_id', 'seller_total', 'seller_id',"order_status", 'closed_on']
    # superuser_fields = ['order_total']
    list_filter = ('user_message',)
    # search_fields = ['user_id']
    # autocomplete_fields = ['owner','restaurant','addons']
    # autocomplete_fields = ['addons']
    # list_select_related = ['addons']
    list_per_page = 10

    # def get_form(self, request, obj=None, **kwargs):
    #     if request.user.is_superuser:
    #         self.fields = self.normaluser_fields + self.superuser_fields
    #     else:
    #         self.fields = self.normaluser_fields
    #     return super(OrderAdmin, self).get_form(request, obj, **kwargs)

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

    def get_restaurant_id(self,request):
        # breakpoint()
        return self.order_id.seller_id

    def get_queryset(self, request):
        qs = super(DisputeAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        else:
            restaurant = Restaurant.objects.get(owner=request.user)
            # restaurantID = self.get_restaurant_id(request)
            # breakpoint()
            # return qs.filter(order_id.seller_id == restaurant.id)
            return qs.filter(order_id__seller_id= restaurant.id)
            # return qs

admin.site.register(Dispute, DisputeAdmin)