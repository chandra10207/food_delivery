from django.urls import include, path
from api import views
urlpatterns = [
    # path('users/', include('users.urls')),
    path('users/', views.UserListView.as_view()),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls'))
]