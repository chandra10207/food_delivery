from django.contrib import admin
# from food.models import Food, Addon , AddonAdmin, FoodAdmin, ProductAddon_inline
from food.models import Food, Addon

# Register your models here.
admin.site.register(Food)
admin.site.register(Addon)


# admin.site.register(Addon, AddonAdmin)
# admin.site.register(Food, FoodAdmin)
# admin.site.register(ProductAddon_inline)