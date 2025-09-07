from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from drf_spectacular.views import ( 
    SpectacularAPIView, 
    SpectacularRedocView, 
    SpectacularSwaggerView,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include('api.urls')),
    path('silk/', include('silk.urls', namespace='silk')),
    path('api/token/', TokenObtainPairView.as_view(), name="toekn-obtain-pair"),
    path('api/token/refresh/', TokenRefreshView.as_view(), name="token-refresh"),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(), name='redoc')
]