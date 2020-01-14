from django.contrib import admin
# from food.models import Food, Addon , AddonAdmin, FoodAdmin, ProductAddon_inline
from food.models import Food, Addon
from restaurant.models import Restaurant
from django.contrib.admin import SimpleListFilter

# Register your models here.
# admin.site.register(Food)
# admin.site.register(Addon)


# admin.site.register(Addon, AddonAdmin)
# admin.site.register(Food, FoodAdmin)
# admin.site.register(ProductAddon_inline)

class CountryFilter(SimpleListFilter):
    title = 'owner 1' # or use _('country') for translated title
    parameter_name = 'owner 1'

    def lookups(self, request, model_admin):
        countries = set([c.owner for c in model_admin.model.objects.all()])
        return [(c.id, c.username) for c in countries]
        # You can also use hardcoded model name like "Country" instead of
        # "model_admin.model" if this is not direct foreign key filter

    def queryset(self, request, queryset):
        # breakpoint()
        # qs = super(Food, self).queryset(request)
        if request.user.is_superuser:
            return queryset
        return queryset.filter(owner=request.user)
        #
        # if self.value():
        #     return queryset.filter(country__id__exact=self.value())
        # else:
        #     return queryset



class FoodAdmin(admin.ModelAdmin):
    # date_hierarchy = 'pub_date'
    # list_display = ('full_name', 'langugae', 'grades', 'gender')
    list_display = ('id', 'name', 'regular_price', 'restaurant', 'owner')
    # list_filter = (CountryFilter,)
    ordering = ['name']
    # list_filter = ('langugae', 'gender', 'grades')
    # list_filter = ( 'restaurant', 'owner')
    save_as = True
    save_on_top = True
    # change_list_template = 'change_list_graph.html'
    # readonly_fields = ('owner','restaurant')

    normaluser_fields = ['name','slug','description','regular_price','image','addons']
    superuser_fields = ['owner','restaurant']
    search_fields = ['name']
    # autocomplete_fields = ['owner','restaurant','addons']
    # autocomplete_fields = ['addons']
    # list_select_related = ['addons']
    list_per_page = 10

    def get_form(self, request, obj=None, **kwargs):
        if request.user.is_superuser:
            self.fields = self.normaluser_fields + self.superuser_fields
        else:
            self.fields = self.normaluser_fields
        return super(FoodAdmin, self).get_form(request, obj, **kwargs)

    def save_model(self, request, obj, form, change):
        """When creating a new object, set the creator field.
        """
        # restaurant = request.user.restaurant_owner
        # restaurantfood = Restaurant.objects.get(owner=request.user)
        # print(restaurant)
        # breakpoint()
        if not change:
            if not request.user.is_superuser:
                restaurantfood = Restaurant.objects.get(owner=request.user)
                obj.owner = request.user
                obj.restaurant = restaurantfood
        obj.save()

    def get_queryset(self, request):
        qs = super(FoodAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        # return queryset.filter(owner=request.user)
        return qs.filter(owner=request.user)

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == "addons":
            if not request.user.is_superuser:
                # kwargs["queryset"] = Addon.objects.all()
                kwargs["queryset"] = Addon.objects.filter(created_by=request.user)
        return super(FoodAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    # actions = [make_published]
    class Media:
        css = {
            'all': ('/static/admin-lte/plugins/select2/css/select2.css','/static/admin/css/custom.css')
             }
        js = ('/static/admin-lte/plugins/select2/js/select2.full.js','/static/admin/js/custom.js')

    # def export_as_json(modeladmin, request, queryset):
    #     response = HttpResponse(content_type="application/json")
    #     serializers.serialize("json", queryset, stream=response)
    #     return response

    # def queryset(self, request):
    #     breakpoint()
    #     qs = super(Food, self).queryset(request)
    #     if request.user.is_superuser:
    #         return qs
    #     return qs.filter(owner=request.user)



admin.site.register(Food, FoodAdmin)


# @admin.register(Customer)
class AddonAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'created_by']
    search_fields = ['name']


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
        if not change:
            obj.created_by = request.user
        obj.save()

    def get_queryset(self, request):
        qs = super(AddonAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        # return queryset.filter(owner=request.user)
        return qs.filter(created_by=request.user)

admin.site.register(Addon, AddonAdmin)




