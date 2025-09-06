from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include('api.urls')),
    path('silk/', include('silk.urls', namespace='silk')),
]