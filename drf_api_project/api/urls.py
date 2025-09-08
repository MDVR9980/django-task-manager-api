from django.urls import path
from api import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('', views.apiOverview, name="api-overview"),

    # for products :
    # path('product-list/', views.ProductList, name="product-list"),
    # path('product-list/', views.ProductListAPIView.as_view(), name="product-list"),
    path('products/', views.ProductListCreateAPIView.as_view(), name="product-list"),
    # path('products/info/', views.Product_info, name="product-info"),
    path('products/info/', views.ProductInfoView.as_view(), name="product-info"),
    # path('product-detail/<int:pk>', views.ProductDetail, name="product-detail"),
    path('product-detail/<int:product_id>', views.ProductDetailAPIView.as_view(), name="product-detail"),
    # path('product-create/', views.ProductCreateAPIView.as_view(), name="product-create"),
    path('product-update/<int:product_id>', views.ProductUpdateAPIView.as_view(), name="product-update"),
    path('product-delete/<int:product_id>', views.ProductDeleteAPIView.as_view(), name="product-delete"),
    path('product-update-delete/<int:product_id>', views.ProductUpdateDeleteAPIView.as_view(), name="product-update-delete"),


    # # for orders :
    # # path('order-list/', views.OrderList, name="order-list"),
    # path('order-list/', views.OrderListAPIView.as_view(), name="order-list"),
    # path('user-order-list/', views.UserOrderListAPIView.as_view(), name="user-order-list"),
]

router = DefaultRouter()
router.register('orders', views.OrderViewSet)
urlpatterns += router.urls