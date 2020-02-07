import json

from django.contrib import admin
from restaurant.models import Restaurant
from Location.models import Address
from food.models import Food
# from django_google_maps import widgets as map_widgets
# from django_google_maps import fields as map_fields
# Register your models here.
# admin.site.register(Restaurant)

class FoodInline(admin.TabularInline):
    model = Food
# inlines = [
#         FoodInline,
#     ]
# @admin.register(Customer)
class RestaurantAdmin(admin.ModelAdmin):
    # formfield_overrides = {
    #     map_fields.AddressField: {'widget': map_widgets.GoogleMapsAddressWidget},
    # }
    list_display = ['id', 'name', 'owner']
    normaluser_fields = ['name','address','email','website','content','restaurant_logo','restaurant_banner_image']
    superuser_fields = ['owner']
    search_fields = ['name']
    autocomplete_fields = ['owner']
    list_select_related = ['owner']
    list_per_page = 10
    # inlines = [
    #     FoodInline,
    # ]

    def get_form(self, request, obj=None, **kwargs):
        if request.user.is_superuser:
            self.fields = self.normaluser_fields + self.superuser_fields
        else:
            self.fields = self.normaluser_fields
        return super(RestaurantAdmin, self).get_form(request, obj, **kwargs)

    def save_model(self, request, obj, form, change):
        """When creating a new object, set the creator field.
        """
        if not change:
            obj.owner = request.user
        obj.save()

    def get_queryset(self, request):
        qs = super(RestaurantAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        # return queryset.filter(owner=request.user)
        return qs.filter(owner=request.user)

    def formfield_for_foreignkey(self, db_field, request=None, **kwargs):
        if db_field.name == "address":
            if not request.user.is_superuser:
                kwargs["queryset"] = Address.objects.filter(created_by=request.user)
        return super(RestaurantAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)




admin.site.register(Restaurant, RestaurantAdmin)