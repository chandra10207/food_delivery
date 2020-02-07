from django.contrib import admin
from food_delivery.models import UserProfileInfo, User



class ProfileAdmin(admin.ModelAdmin):
    # date_hierarchy = 'pub_date'
    # list_display = ('full_name', 'langugae', 'grades', 'gender')
    list_display = ['id', 'user', 'phone', 'balance', 'address']
    # list_filter = (CountryFilter,)
    ordering = ['id']


# Register your models here.
admin.site.register(UserProfileInfo,ProfileAdmin)
