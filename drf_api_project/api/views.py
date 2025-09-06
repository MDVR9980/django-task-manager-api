from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.db.models import Max
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.serializers import ProductSerializer, OrderSerializer, ProductInfoSerializer
from api.models import Product, Order, OrderItem
from rest_framework import generics

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/product-list/',
        'Detail View': '/product-detail/<str:pk>/',
        }

    return Response(api_urls)


# for products:
class productListAPIView(generics.ListAPIView):
    # queryset = Product.objects.filter(stock__gt=0)
    # queryset = Product.objects.exclude(stock__gt=0)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # permission_classes = [isAdminUser]

# @api_view(['GET'])
# def productList(request):
#     products = Product.objects.all()
#     serializer = ProductSerializer(products, many=True)
#     return Response(serializer.data)

class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # permission_classes = [isAdminUser]
    lookup_url_kwarg = 'product_id' # by default is pk

# @api_view(['GET'])
# def productDetail(request, pk):
#     product = get_object_or_404(Product, pk=pk)
#     serializer = ProductSerializer(product, many=False)
#     return Response(serializer.data)


@api_view(['GET'])
def product_info(request):
    products = Product.objects.all()
    serializer = ProductInfoSerializer({
        'products': products,
        'count': len(products),
        'max_price': products.aggregate(max_price=Max('price'))['max_price']
    })
    return Response(serializer.data)

# for orders:

class OrderListAPIView(generics.ListAPIView):
    queryset = Order.objects.prefetch_related('items__product').all()
    serializer_class = OrderSerializer
    # permission_classes = [isAdminUser]
    

class UserOrderListAPIView(generics.ListAPIView):
    queryset = Order.objects.prefetch_related('items__product').all()
    serializer_class = OrderSerializer
    
    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(user=self.request.user)

# @api_view(['GET'])
# def orderList(request):
#     orders = Order.objects.prefetch_related('items__product').all()
#     serializer = OrderSerializer(orders, many=True)
#     return Response(serializer.data)