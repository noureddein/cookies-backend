from django.urls import path, include
from locations.api.view import CookiesLocationDetailView,CookiesLocationListView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('cookies-location', CookiesLocationListView.as_view(), name='cookies_location_list'),
    path('cookies-location-details/<int:pk>',
         CookiesLocationDetailView.as_view(), name='cookies_location_details'),
    path('token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('api-auth/', include('rest_framework.urls')),
]