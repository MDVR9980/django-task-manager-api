from django.urls import path
from api import views

urlpatterns = [
    path('', views.apiOverview, name="api-overview"),

    # for products :
    # path('product-list/', views.productList, name="product-list"),
    # path('product-list/', views.productListAPIView.as_view(), name="product-list"),
    path('products/', views.productListCreateAPIView.as_view(), name="product-list"),
    # path('products/info/', views.product_info, name="product-info"),
    path('products/info/', views.ProductInfoView.as_view(), name="product-info"),
    # path('product-detail/<int:pk>', views.productDetail, name="product-detail"),
    path('product-detail/<int:product_id>', views.ProductDetailAPIView.as_view(), name="product-detail"),
    # path('product-create/', views.productCreateAPIView.as_view(), name="product-create"),
    # for orders :
    # path('order-list/', views.orderList, name="order-list"),
    path('order-list/', views.OrderListAPIView.as_view(), name="order-list"),
    path('user-order-list/', views.UserOrderListAPIView.as_view(), name="user-order-list"),
]
