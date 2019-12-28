from django.contrib import admin
# from food.models import Food, Addon , AddonAdmin, FoodAdmin, ProductAddon_inline
from food.models import Food, Addon

from django.contrib.admin import SimpleListFilter

# Register your models here.
# admin.site.register(Food)
admin.site.register(Addon)


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
    list_display = ('name', 'regular_price', 'restaurant', 'owner')
    list_filter = (CountryFilter,)
    # ordering = ['name']
    # list_filter = ('langugae', 'gender', 'grades')
    # list_filter = ( 'restaurant', 'owner')
    save_as = True
    save_on_top = True
    # change_list_template = 'change_list_graph.html'

    # actions = [make_published]

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