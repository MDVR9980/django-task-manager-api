from django.urls import path
from api import views

urlpatterns = [
    path('', views.apiOverview, name="api-overview"),

    # for products :
    path('product-list/', views.productList, name="product-list"),
    path('product-detail/<int:pk>', views.productDetail, name="product-detail"),
    # for orders :
    path('order-list/', views.orderList, name="order-list"),
]
