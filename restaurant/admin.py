import json

from django.contrib import admin
from restaurant.models import Restaurant

# Register your models here.
# admin.site.register(Restaurant)

# @admin.register(Customer)
class RestaurantAdmin(admin.ModelAdmin):

    list_display = ['name', 'owner']

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