from django.urls import path, include, re_path

from django.contrib import admin

admin.autodiscover()

import hello.views

# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/


admin.site.site_header = "Food Delivery Admin"
admin.site.site_title = "Food Delivery Admin Portal"
admin.site.index_title = "Welcome to Food Delivery"


urlpatterns = [
    path("", hello.views.index, name="index"),
    path("db/", hello.views.db, name="db"),
    path("admin/", admin.site.urls),
    # url(r'^api-auth/', include('rest_framework.urls')),
    re_path('api/(?P<version>(v1|v2))/', include('food.urls')),
]
