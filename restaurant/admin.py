from django.contrib import admin
from restaurant.models import Restaurant
# Register your models here.
admin.site.register(Restaurant)


# class RestaurantAdmin(admin.ModelAdmin):
#       def get_readonly_fields(self, request, obj=None):
#         if not request.user.is_superuser and request.user.has_perm('restaurants.read_item'):
#             return [f.name for f in self.model._meta.fields]
#         return super(Restaurant, self).get_readonly_fields(
#             request, obj=obj
#         )
#     # def has_add_permission(request):
#     #     # Should return True if adding an object is permitted, False otherwise.
#     #
#     # def has_change_permission(request, obj=None)
#     #     # Should return True if editing obj is permitted, False otherwise.
#     #     # If obj is None, should return True or False to indicate whether editing of objects of this type is permitted in general
#     #
#     # def has_delete_permission(request, obj=None)
#     #     # Should return True if deleting obj is permitted, False otherwise.
#     #     # If obj is None, should return True or False to indicate whether deleting objects of this type is permitted in general
#
#
# admin.site.register(Restaurant, RestaurantAdmin)