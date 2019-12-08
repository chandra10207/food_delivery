from django.urls import path
from food import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    # path('$/', views.foods, name='foods'),
    # path('$/', views.restaurants, name='restaurants')
    # path('restaurants/', ListSongsView.as_view(), name="songs-all")

    # path('', views.index, name='index'),
    # path('food/', views.individual_restaurant, name='individual_restaurant'),
    # path('restaurants/', views.RestaurantList.as_view(), name="restaurant-all"), #class based view
    # path('restaurants/', views.list_restaurant), #function based view

    # path('restaurant/<int:pk>', GetRestaurantDetail.as_view(), name="restaurant-detail")
    # path('restaurant/<int:pk>', views.RestaurantDetail.as_view(), name="restaurant-detail")
    # path('restaurant/<int:pk>', views.restaurant_single)

]

urlpatterns = format_suffix_patterns(urlpatterns)

