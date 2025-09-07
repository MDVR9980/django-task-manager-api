from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include('api.urls')),
    path('silk/', include('silk.urls', namespace='silk')),
    path('api/token/', TokenObtainPairView.as_view(), name="toekn-obtain-pair"),
    path('api/token/refresh/', TokenRefreshView.as_view(), name="token-refresh")
]