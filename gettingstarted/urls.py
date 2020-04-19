from django.urls import path, include, re_path
from django.contrib import admin
from django.conf.urls import url, include
from food_delivery import views

from django.conf.urls.static import static
from django.conf import settings


admin.autodiscover()

import hello.views
import food_delivery.views

# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/


admin.site.site_header = "Food Delivery"
admin.site.site_title = "Food Delivery Admin Portal"
admin.site.index_title = "Available Options"


urlpatterns = [
    path("", hello.views.index, name="index"),
    # path("register/", food_delivery.views.register, name="register"),
    path('food_delivery/', include('food_delivery.urls'), name="register"),
    path("db/", hello.views.db, name="db"),
    path('admin/doc/', include('django.contrib.admindocs.urls')),
    path("admin/", admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls')),
    re_path('api/(?P<version>(v1|v2))/', include('food.urls')),
    re_path('api/(?P<version>(v1|v2))/', include('api.urls')),
    re_path('api/(?P<version>(v1|v2))/', include('restaurant.urls')),
    # path('api/v1/', include('api.urls')),
    # url(r'^$',views.index,name='index'),
    # url(r'^special/',views.special,name='special'),
    # url(r'^food_delivery/',include('food_delivery.urls')),
    # re_path("food_delivery/", include('food_delivery.urls')),
    url(r'^logout/$', views.user_logout, name='logout'),
    path("stripe/", include("djstripe.urls", namespace="djstripe")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
