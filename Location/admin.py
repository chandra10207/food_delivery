from django.contrib import admin
from Location.models import Address
# Register your models here.

# admin.site.register(Address)


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ['unit', 'street_number', 'street_name','suburb','state','post_code','created_by']
    search_fields = ['street_name']

    normaluser_fields = ['unit', 'street_number', 'street_name','suburb','state','post_code']
    superuser_fields = ['created_by']
    #
    def get_form(self, request, obj=None, **kwargs):
        if request.user.is_superuser:
            self.fields = self.normaluser_fields + self.superuser_fields
        else:
            self.fields = self.normaluser_fields
        return super(AddressAdmin, self).get_form(request, obj, **kwargs)


    # def get_readonly_fields(self, request, obj=None):
    #     if request.user.is_superuser:
    #         return []
    #     return ["owner"]
    #     # if obj:
    #     #     return ["name", "category"]
    #     # else:
    #     #     return []

    def save_model(self, request, obj, form, change):
        """When creating a new object, set the creator field.
        """
        if not change and not obj.created_by:
            obj.created_by = request.user
        obj.save()

    def get_queryset(self, request):
        qs = super(AddressAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        # return queryset.filter(owner=request.user)
        return qs.filter(created_by=request.user)