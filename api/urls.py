from allauth.account.views import confirm_email
from django.urls import include, path
from api import views as api_views
from rest_framework.authtoken import views
from django.conf.urls import url
from api.views import CustomObtainAuthToken
from sales import views as sales_views
from store_follower import views as store_follower_views
from promocode import views as promo_views


urlpatterns = [
    # path('users/', include('users.urls')),
    path('users/', api_views.UserListView.as_view()),
    path('user/<int:pk>', api_views.UserDetailView.as_view(), name="user-detail"),
    path('user/<int:pk>/orders', api_views.UserOrdersAPI.as_view(), name="user-orders"),
    path('orders/', sales_views.OrderListApi.as_view()),
    path('order/<int:pk>', sales_views.OrderListDetailApi.as_view(), name="order-detail"),
    path('storefollowers/', store_follower_views.StoreFollowerListAPI.as_view()),
    path('storefollower/<int:pk>', store_follower_views.StoreFollowerDetailAPI.as_view(), name="order-detail"),
    path('promocodes/', promo_views.CouponListAPI.as_view()),
    path('promocode/', promo_views.UseCouponView.as_view()),
    # path('promocode/<int:pk>', store_follower_views.StoreFollowerDetailAPI.as_view(), name="order-detail"),

    # path('users/', api_views.UserListView.as_view()),
    # path('rest-auth/', include('rest_auth.urls')),
    # path('rest-auth/registration/', include('rest_auth.registration.urls')),
   url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
    # url(r'^user/$', UserDetailsView.as_view(), name='rest_user_details'),

    # path('customer_login/', views.customer_login),
    # url(r'^api-token-auth/', views.obtain_auth_token, name='auth-token'),
url(r'^authenticate/', CustomObtainAuthToken.as_view()),

url(r'^accounts/', include('allauth.urls')),
# url(r'^rest-auth/registration/account-confirm-email/(?P<key>\w+)/$',confirm_email, name='account_confirm_email'),
# url(r'^rest-auth/', include('rest_auth.urls')),
# url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),


]