from django.contrib import admin
from django.urls import reverse
from django.utils.safestring import mark_safe
from review.models import Review
from restaurant.models import Restaurant


# Register your models here.

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'restaurant_id', 'rating', 'created_on', 'review_title')
    autocomplete_fields = ['user_id', 'restaurant_id']
    # readonly_fields = ['user_id', 'follower_name', 'restaurant_name', 'restaurant_id']

    # def save_model(self, request, obj, form, change):
    #     """When creating a new object, set the creator field.
    #     """
    #     if not change:
    #         obj.created_by = request.user
    #     obj.save()

    def get_queryset(self, request):
        qs = super(ReviewAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        else:
            restaurant = Restaurant.objects.get(owner=request.user)
            # return queryset.filter(owner=request.user)
            return qs.filter(store_id=restaurant)

    # def get_readonly_fields(self, request, obj=None):
    #     fields = super().get_readonly_fields(request)
    #     if not request.user.is_superuser:
    #         fields.append('featured')
    #     return fields

    # def get_readonly_fields(self, request, obj=None):
    #     if request.user.is_staff:
    #         if request.user.is_superuser:
    #             return []
    #         else:
    #             return [f.follower_name for f in self.model._meta.fields]


admin.site.register(Review, ReviewAdmin)
