import json

from django.contrib import admin
from restaurant.models import Restaurant
# from django_google_maps import widgets as map_widgets
# from django_google_maps import fields as map_fields
# Register your models here.
# admin.site.register(Restaurant)

# @admin.register(Customer)
class RestaurantAdmin(admin.ModelAdmin):
    # formfield_overrides = {
    #     map_fields.AddressField: {'widget': map_widgets.GoogleMapsAddressWidget},
    # }
    list_display = ['name', 'owner']
    normaluser_fields = ['name','restaurant_address','email','website','content','restaurant_logo','restaurant_banner_image']
    superuser_fields = ['owner']
    search_fields = ['name']
    autocomplete_fields = ['owner']
    list_select_related = ['owner']
    list_per_page = 10

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

admin.site.register(Restaurant, RestaurantAdmin)