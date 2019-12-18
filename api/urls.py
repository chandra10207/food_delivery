from allauth.account.views import confirm_email
from django.urls import include, path
from api import views
urlpatterns = [
    # path('users/', include('users.urls')),
    path('users/', views.UserListView.as_view()),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),

# url(r'^accounts/', include('allauth.urls')),
# url(r'^rest-auth/registration/account-confirm-email/(?P<key>\w+)/$',confirm_email, name='account_confirm_email'),
# url(r'^rest-auth/', include('rest_auth.urls')),
# url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),


]